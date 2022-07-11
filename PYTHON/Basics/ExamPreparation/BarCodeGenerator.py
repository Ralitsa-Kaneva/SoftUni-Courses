number1 = int(input())
number2 = int(input())

for i in range(number1,number2):
    firstDigit = (i // 1000) % 10
    secondDigit = (i // 100) % 10
    thirdDigit = (i // 10) % 10
    forthDigit = i % 10
    if (firstDigit % 2 != 0) and (secondDigit % 2 != 0) and (thirdDigit % 2 != 0) and (forthDigit % 2 != 0):
        print(i, end = " ")
