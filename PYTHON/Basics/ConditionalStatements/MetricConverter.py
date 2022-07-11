number = float(input())
entryUnit = input()
exitUnit = input()
convertedNumber = 0

if entryUnit == 'mm':
    if exitUnit == 'cm':
        convertedNumber = number / 10
    elif exitUnit == 'm':
        convertedNumber = number / 1000
elif entryUnit == 'cm':
    if exitUnit == 'mm':
        convertedNumber = number * 10
    elif exitUnit == 'm':
        convertedNumber = number / 100
elif entryUnit == 'm':
    if exitUnit == 'mm':
        convertedNumber = number * 1000
    elif exitUnit == 'cm':
        convertedNumber = number * 100

print(f'{convertedNumber:.3f}')

