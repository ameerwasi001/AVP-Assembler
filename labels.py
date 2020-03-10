class LabelCheck:
    def __init__(self):
        self.label_map = {}
        self.instruction = None
        self.line_no = None

    def set_instruction(self, line_no, instruction):
        self.instruction = instruction
        self.line_no = str(hex(int(line_no)))

    def define(self):
        if self.instruction[0].startswith("#"):
            self.label_map[self.instruction[0]] = self.line_no
            print(self.label_map)
            return True

    def call(self):
        index = 0
        while index<len(self.instruction):
            if (self.instruction[index] == '02') and (self.instruction[index+1].startswith("#")):
                self.instruction[index+1] = self.label_map[self.instruction[index+1]]
                return self.instruction
            index+=1
