import math

wallHight = int(input())
wallWide = int(input())
notPainting = int(input())
walls = 4 * wallWide * wallHight
wallsForPainting =math.ceil(walls - (walls * notPainting / 100))
wallsRemain = wallsForPainting
inpt = input()

while inpt != 'Tired!':
    paintLitre = int(inpt)
    wallsRemain = wallsRemain - paintLitre
    if wallsRemain < 0:
        print(f'All walls are painted and you have {abs(wallsRemain)} l paint left!')
        break
    elif wallsRemain == 0:
        print(f'All walls are painted! Great job, Pesho!')
        break
    inpt = input()

if inpt == 'Tired!':
    print(f'{wallsRemain} quadratic m left.')





