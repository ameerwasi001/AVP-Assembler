class Token:
    def __init__(self, token_type, token_value):
        self.type = token_type
        self.value = token_value

class Lexer:
    def __init__(self, line):
        self.line = line
        self.instructions = None

    def __evaporate_white_space(self, string):
        while string.startswith(" "):
            string = string[1:]
        while string.endswith(" "):
            string = string[:1]
        return string

    def split_up(self):
        self.instructions = list(self.line)
        outstr = [""]
        for i, x in enumerate(self.instructions):
            if x==" ":
                outstr.append(self.__evaporate_white_space(x))
            else:
                outstr[-1] += self.__evaporate_white_space(x)
        self.instructions = outstr
        self.instructions = [x for x in self.instructions if x != ""]
        return self.instructions

    def check_and_change(self):
        def hasNumbers(inputString):
            return any(char.isdigit() for char in inputString)
        p = 0
        while p<len(self.instructions):
            if self.instructions[p].startswith('"'):
                self.instructions = self.str_process(self.instructions, p)
            elif self.instructions[p].isdigit():
                self.instructions[p] = Token("DIGIT", self.digit_process(p))
            elif (self.instructions[p].islower()):
                self.instructions[p] = Token("STRING", self.specialToString_process(p))
            elif self.instructions[p].startswith("#"):
                self.instructions[p] = Token("LABEL", self.instructions[p])
            else:
                self.instructions[p] = Token("INSTRUCTION", self.instructions[p])
            p+=1
        self.instructions.append(Token("INSTRUCTION", "EOI"))
        return self.instructions

    def specialToString_process(self, pointer):
        specials = {
                'newline': "{0x5c6e}",
                'tab': "{0x5c74}",
                'alert': "{0x5c61}",
                'formfeed': "{0x5c66}"
            }
        if self.instructions[pointer] in specials:
            return specials[self.instructions[pointer]]
        else:
            raise NameError(f'Unknown special "{self.instructions[pointer]}"')
        

    def digit_process(self, pointer):
        digit = hex(int(self.instructions[pointer]))
        return digit        

    def str_process(self, ins, p):
        rest = self.instructions[p:]
        strwhole = [rest[0]]
        for i, x in enumerate(rest):
            if x.endswith('"'):
                break
            else:
                strwhole.append(rest[i+1])
        strwhole = ' '.join(strwhole)
        strwhole = strwhole[1:]
        strwhole = strwhole[:-1]
        substitute_rest = []
        rest = rest[1:]
        substitute_rest_check = False
        for x in rest:
            if x.endswith('"'):
                substitute_rest_check = not(substitute_rest_check)
            if substitute_rest_check:
                substitute_rest.append(x)
        rest = substitute_rest
        rest = rest[1:]
        string = "{0x"+strwhole.encode("utf-8").hex()+"}"
        self.instructions = [self.instructions[0], Token("STRING", string), *rest]
        print(self.instructions[p].type, self.instructions[p].value)
        return self.instructions
