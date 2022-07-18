import re

text = input()
expression = r"(^|(?<=\s))-?[1-9]([0-9]+)?(.\d+)?($|(?=\s))"
output = re.finditer(expression,text)
outputlist = []

for element in output:
    outputlist.append(element.group())

print(" ".join(outputlist))
