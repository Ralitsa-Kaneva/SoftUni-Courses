tshirtsPrice = float(input())
sumForBall = float(input())
shortsPrice = tshirtsPrice * 75 / 100
socksPrice = shortsPrice * 20 / 100
buttonsPrice = 2 * (tshirtsPrice + shortsPrice)
sum = tshirtsPrice + shortsPrice + socksPrice + buttonsPrice
discount = sum * 15 / 100
totalSum = sum - discount

sumNeeded = sumForBall - totalSum

if sumNeeded < 0 or sumNeeded == 0:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {totalSum:.2f} lv.')
else:
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {sumNeeded:.2f} lv. more.')

