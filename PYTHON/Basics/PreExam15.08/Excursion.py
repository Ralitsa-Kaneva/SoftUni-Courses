groupPeopleCount = int(input())
nightsCount = int(input())
transportCard = int(input())
museumTickets = int(input())
expenses = groupPeopleCount * (nightsCount * 20 + transportCard * 1.60 + museumTickets * 6)
risk = expenses * 25 / 100
totalExpenses = expenses + risk

print(f'{totalExpenses:.2f}')
