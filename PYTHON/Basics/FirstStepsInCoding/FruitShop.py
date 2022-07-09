strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberries_price/2
oranges_price = raspberries_price - (40 * raspberries_price / 100)
bananas_price = raspberries_price - (80 * raspberries_price / 100)

needed_money = strawberries_kg * strawberries_price + bananas_price * bananas_kg + oranges_price * oranges_kg + raspberries_price * raspberries_kg

print (needed_money)