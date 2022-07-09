rent = int(input())
cake = 20 * rent / 100
drinks = cake - (45 * cake / 100)
animator = rent / 3

budget = rent + cake + drinks + animator

print (round(budget,2))