session = input()
ticketType = input()
ticketsNumber = int(input())
picture = input()

price = 0
totalPrice = 0
bonus = 0
picturePrice = ticketsNumber * 40
freePicture = False

if ticketType == 'Standard':
    if (session == 'Quarter final'):
        price = 55.50
    elif (session == 'Semi final'):
        price = 75.88
    elif (session == 'Final'):
        price = 110.10
elif ticketType == 'Premium':
    if (session == 'Quarter final'):
        price = 105.20
    elif (session == 'Semi final'):
        price = 125.22
    elif (session == 'Final'):
        price = 160.66
elif ticketType == 'VIP':
    if (session == 'Quarter final'):
        price = 118.90
    elif (session == 'Semi final'):
        price = 300.40
    elif (session == 'Final'):
        price = 400

totalPrice = price * ticketsNumber

if picture == 'Y':
    isPicture = True
if totalPrice > 4000:
    freePicture = True
    bonus = totalPrice * 25 / 100
    totalPrice = totalPrice - bonus
elif totalPrice > 2500:
    bonus = totalPrice * 10 / 100
    totalPrice = totalPrice - bonus

if picture == 'Y' and freePicture != True:
    totalPrice = totalPrice + picturePrice

print (f'{totalPrice:.2f}')
