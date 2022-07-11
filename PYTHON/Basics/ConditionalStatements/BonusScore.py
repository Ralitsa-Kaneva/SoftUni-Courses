startBalance = int(input())
bonusPoints = 0
totalPoints = 0

if startBalance <= 100:
    bonusPoints = 5
elif startBalance > 100 and startBalance < 1000:
    bonusPoints = startBalance * 20 / 100
else:
    bonusPoints = startBalance * 10 / 100

if startBalance % 2 == 0:
    bonusPoints += 1
elif startBalance % 10 == 5:
    bonusPoints += 2

totalPoints = startBalance + bonusPoints

print(f'{bonusPoints}')
print(f'{totalPoints}')