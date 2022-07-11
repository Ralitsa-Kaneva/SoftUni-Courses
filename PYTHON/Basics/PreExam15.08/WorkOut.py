import math

trainingDays = int(input())
kmRan = float(input())
sumKm = kmRan

for i in range (0, trainingDays):
    increaseDayNormPercents = int(input())
    increaseDayNorm = increaseDayNormPercents / 100
    kmRan = kmRan + kmRan*increaseDayNorm
    sumKm = sumKm + kmRan

if sumKm >= 1000:
    print(f'You\'ve done a great job running {math.ceil(sumKm - 1000)} more kilometers!')
else:
    print(f'Sorry Mrs. Ivanova, you need to run {math.ceil(1000 - sumKm)} more kilometers')
