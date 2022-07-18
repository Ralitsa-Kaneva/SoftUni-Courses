import re

text = input()
expression = r"(?P<days>\d{2})([.//-])(?P<months>[A-Z][a-z]{2})\2(?P<year>\d{4})"
output = re.finditer(expression, text)

for element in output:
    day = element.group("days")
    month = element.group("months")
    year = element.group("year")
    print(f"Day: {day}, Month: {month}, Year: {year}")
