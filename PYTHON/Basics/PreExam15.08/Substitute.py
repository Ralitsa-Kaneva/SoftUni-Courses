k = int(input())
l = int(input())
m = int(input())
n = int(input())

count = 0

for a in range (k,8+1):
    for b in range (9,l-1,-1):
        for c in range (m,8+1):
            for d in range (9,n-1,-1):
                if a % 2 ==0 and b % 2 != 0 and c % 2 == 0 and d % 2 != 0:
                    if a==c and b==d:
                        print('Cannot change the same player.')
                    else:
                        count = count + 1
                        print(f'{a}{b} - {c}{d}')
                if count == 6:
                    break
            if count == 6:
                break
        if count == 6:
            break
    if count == 6:
        break




