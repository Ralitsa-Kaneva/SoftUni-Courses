import re

text = input()
expression = r"\+359([ -])2\1\d{3}\1\d{4}\b"
output = re.finditer(expression, text)
outputlist = []

for element in output:
    outputlist.append(element.group())

print(", ".join(outputlist))
