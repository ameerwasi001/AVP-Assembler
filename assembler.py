from lexer import Lexer
from transformer import codeTransform
from labels import LabelCheck
import sys

if len(sys.argv) < 3:
    raise Exception("Well, there's no file that I can translate here")

file_name = sys.argv[1]
textins = open(file_name).read()
textouts = []
print(textins)
lines = textins.split("\n")
lines = [line for line in lines if not line==""]
for line_no, line in enumerate(lines):
    lexer = Lexer(line)
    lexer.split_up()
    instructions = lexer.check_and_change()
    transformer = codeTransform(instructions, line_no)
    transformer.Transform()
    instructions = transformer.get_transformed()
    instructions = [i for i in instructions if i!= []]
    unturned = True
    for i in instructions:
        if isinstance(i, list):
            unturned = False
            textouts.append(i)
    if unturned:
        textouts.append(instructions)
labels = LabelCheck()
i = 0
while i<len(textouts):
    l = textouts[i]
    labels.set_instruction(i, l)
    label_definition = labels.define()
    if label_definition:
        textouts.pop(i)
    else:
        textouts[i] = l
        i+=1
i = 0
while i<len(textouts):
    l = textouts[i]
    labels.set_instruction(i, l)
    label_call = labels.call()

    if label_call:
        l = label_call
    textouts[i] = ' '.join(l)
    i+=1
textouts = '\n'.join(textouts)
print(textouts)
output_file = open(sys.argv[2], 'w+')
output_file.write(textouts)
output_file.close()
