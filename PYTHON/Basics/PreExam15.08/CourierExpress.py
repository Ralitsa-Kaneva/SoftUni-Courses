packageWeight = float(input())
type = input()
km = int(input())

price = 0
count = 0
priceForKm = 0
countForKm = 0

if type == "standard":
    if packageWeight <= 1:
        price = 0.03
    elif packageWeight > 1 and packageWeight <= 10:
        price = 0.05
    elif packageWeight > 10 and packageWeight <= 40:
        price = 0.10
    elif packageWeight > 40 and packageWeight <= 90:
        price = 0.15
    elif packageWeight > 90 and packageWeight <= 150:
        price = 0.20
    totalPrice = price * km
elif type == "express":
    if packageWeight <= 1:
        price = 0.03 * km
        count = 0.03 * 80 / 100
        countForWeight = packageWeight * count
        countForKm = km * countForWeight
        priceWithCount = price + countForKm
    elif packageWeight > 1 and packageWeight <= 10:
        price = 0.05 * km
        count = 0.05 * 40 / 100
        countForWeight = packageWeight * count
        countForKm = km * countForWeight
        priceWithCount = price + countForKm
    elif packageWeight > 10 and packageWeight <= 40:
        price = 0.10 * km
        count = 0.10 * 5 / 100
        countForWeight = packageWeight * count
        countForKm = km * countForWeight
        priceWithCount = price + countForKm
    elif packageWeight > 40 and packageWeight <= 90:
        price = 0.15 * km
        count = 0.15 * 2 / 100
        countForWeight = packageWeight * count
        countForKm = km * countForWeight
        priceWithCount = price + countForKm
    elif packageWeight > 90 and packageWeight <= 150:
        price = 0.20 * km
        count =0.20 * 1 / 100
        countForWeight = packageWeight * count
        countForKm = km * countForWeight
        priceWithCount = price + countForKm
    totalPrice = priceWithCount

print(f'The delivery of your shipment with weight of {packageWeight:.3f} kg. would cost {totalPrice:.2f} lv.')