seaExcursions = int(input())
mountainExcursions = int(input())
package = input()
profit = 0

while package !='Stop':
    if package == 'sea' and seaExcursions > 0:
        seaExcursions = seaExcursions - 1
        profit = profit + 680
    elif package == 'mountain' and mountainExcursions > 0:
        mountainExcursions = mountainExcursions - 1
        profit = profit + 499
    if seaExcursions == 0 and mountainExcursions == 0:
        print(f'Good job! Everything is sold.')
        break
    package = input();

print(f'Profit: {profit} leva.')