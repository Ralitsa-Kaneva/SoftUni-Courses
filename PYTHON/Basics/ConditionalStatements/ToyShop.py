discount = 0

excursion_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
truck_toys = int(input())

toys = puzzles + talking_dolls + teddy_bears + minions + truck_toys
puzzle_earnings = puzzles * 2.60
talking_dolls_earnings = talking_dolls * 3
teddy_bears_earnings = teddy_bears * 4.10
minions_earnings = minions * 8.20
truck_toys_earnings = truck_toys * 2
earnings = puzzle_earnings + talking_dolls_earnings + teddy_bears_earnings + minions_earnings + truck_toys_earnings
rent = 10 * earnings / 100

if toys >= 50:
    discount = earnings * 25 / 100
    rent = 10 * (earnings - discount) / 100

total_earnigs = earnings - rent - discount

if total_earnigs >= excursion_price:
    money_left = total_earnigs - excursion_price
    print(f'Yes! {money_left :.2f} lv left.')
else:
    money_to_go = excursion_price - total_earnigs
    print(f'Not enough money! {money_to_go :.2f} lv needed.')

