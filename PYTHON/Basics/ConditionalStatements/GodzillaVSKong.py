budget = float(input())
statists = int(input())
clothesPrice = float(input())
discount = 0
decor = budget * 10 / 100

if statists > 150:
    discount = clothesPrice * 10 / 100
    clothesPrice -= discount

totalExpenses = decor + clothesPrice * statists

if budget < totalExpenses:
    print('Not enough money!')
    print(f'Wingard needs {totalExpenses - budget:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget - totalExpenses:.2f} leva left.')


