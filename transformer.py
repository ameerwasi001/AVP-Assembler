class codeTransform:
    def __init__(self, instructions, line_no):
        self.instructions = instructions
        self.transformed = instructions
        self.opcode_maps = {
                    "END": "00",
                    "EOI": "01",
                    "PUSH": "02",
                    "POP": "03",
                    "PRINT": "04",
                    "ADD": "05",
                    "SUBSTRACT": "06",
                    "MULTIPLY": "07",
                    "DIVIDE": "08",
                    "SHUFFLE": "09",
                    "GOTO": "10",
                    "IFEQUAL": "11",
                    "MODULUS": "12",
                    "INCREMENT": "13",
                    "DECREMENT": "14",
                    "EXPONENT": "15",
                    "STORE": "16",
                    "RETRIVE": "17",
                    "DELETE": "18",
                    "IFGREAT": "19",
                    "IFNULL": "20",
                    "IFPLUS": "21",
                    "IFMINUS": "22",
                    "IFUNEQUAL": "23",
                    "IFEQUAL": "24",
                    "IFSMALL": "25",
                    "GOTO_L": "26",
                    "IFGREAT_0": "27",
                    "IFNULL_0": "28",
                    "IFPLUS_0": "29",
                    "IFMINUS_0": "30",
                    "IFUNEQUAL_0": "31",
                    "IFEQUAL_0": "32",
                    "IFSMALL_0": "33",
                    "SADD": "34",
                    "SCONV": "35",
                    "POP_TOP": "36",
                    "GOTO_CONDITIONALLY": "37",
                    "GOTO_CONDITIONALLY_L": "38",
                    "LITERAL_PRINT": "39",
                    "NOT": "40",
                    "OR": "41",
                    "AND": "42",
                    "REGISTER": "43",
                    "UNREGISTER": "44",
                    "GETREGISTER": "45",
                    "FLOATCONV": "46",
                    "INTCONV": "47",
                    "DUPLICATE": "48",
                    "ARCREATE": "49",
                    "ARCREATE_1": "50",
                    "MEMDUMP": "51",
                    "ARDISASSEMBLE": "52",
                    "ARGET": "53",
                    "ARSET": "54",
                    "ARLEN": "55",
                    "ARAPPEND_0": "56",
                    "ARAPPEND_1": "57",
                    "ARPOP_1": "58",
                    "ARLEN_0": "59",
                    "ARSET_TOP": "60",
                    "ARINSERT_TOP": "61",
                    "ARINSERT": "62",
                    "INPUT": "63",
                    "PUSH_NULL": "64",
                    "SHUFFLE_1": "65",
                    "ARPOP_0": "66",
                    "ARPOP_TOP_1": "67",
                    "ARPOP_TOP_0": "68",
                    "PUSH_TRUE": "69",
                    "PUSH_FALSE": "70",
                    "XOR": "71",
                    "ASSERT": "72",
                    "NEGATE": "73",
                    "IFSAME": "74",
                    "IFSAME_0": "75",
                    "SPLIT": "76",
                    "JOIN": "77",
                    "STRINSERT": "78",
                    "RECORD": "79",
                    "RECAP": "80",
                    "FRAMEDUMP": "81",
                    "RECORDHEAP": "82",
                    "RECAPHEAP": "83",
                    "DUMPHEAP": "84",
                    "PUSH_LAST": "85",
                    "SETUP_EXCEPT": "86",
                    "END_EXCEPT": "87",
                    "IFEXCEPTION": "88",
                    "LISTCONV": "89"
                }
        self.opcodes = [x for x in self.opcode_maps]
        self.line_no = line_no

    def first_key(self, pointer):
        return next(iter(self.instructions[pointer]))

    def literal_transform(self, pointer):
        special = self.instructions[pointer+1]
        before = self.instructions[:pointer]
        after = self.instructions[pointer:]
        after = after[2:]
        before = before[2:]
        for i, d in enumerate(before):
            before[i] = self.__internal_transform(d, pointer)
        for i, d in enumerate(after):
            after[i] = self.__internal_transform(d, pointer)
        if before == ['01']:
            before.pop()
        if after == ['01']:
            after.pop()
        special = self.__internal_transform(special, pointer)
        returner = [before, ["02", f"{special}", "01"], ["39", "01"], ["03", "01"], after]
        return (returner)

    def __internal_transform(self, instruction, pointer):
        transformed = instruction
        instruction_key = instruction.type
        instruction_value = instruction.value
        if (instruction_value in self.opcodes):
            transformed = self.opcode_maps[instruction.value]
        elif instruction_key == "LABEL":
            print("This will take another round at the end to be specific, for now I will just let it be it...")
            transformed = instruction_value
        elif not instruction_key == "INSTRUCTION":
            transformed = instruction_value
        elif instruction_key == "INSTRUCTION":
            raise NameError(f'Unexpeceted instruction "{instruction_value}" in line number {self.line_no+1} at the position {pointer+1}')
        return transformed

    def Transform(self):
        pointer = 0
        while pointer<len(self.instructions):
            instruction_key = self.instructions[pointer].type
            instruction_value = self.instructions[pointer].value
            if (instruction_value in self.opcodes) and (instruction_value != "LITERAL_PRINT"):
                self.transformed[pointer] = self.opcode_maps[instruction_value]
            elif instruction_value == "LITERAL_PRINT":
                self.transformed = self.literal_transform(pointer)
                break
            elif not instruction_key == "INSTRUCTION":
                self.transformed[pointer] = self.instructions[pointer].value
            elif instruction_key == "INSTRUCTION":
                raise NameError(f'Unexpeceted instruction "{instruction_value}" in line number {self.line_no+1} at the position {pointer+1}')
            pointer+=1
            
    def get_transformed(self):
        return self.transformed
