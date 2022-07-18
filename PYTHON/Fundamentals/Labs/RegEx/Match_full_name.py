import re

text = input()
expression = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
output = re.findall(expression, text)

print(" ".join(output))
