number = int(input())
number_length = len(str(number))
sum_digits = 0
special = [5, 7, 11]

for i in range(1, number+1):
    sum_digits = 0
    help_variable = i
    for j in range(0, i):
        if help_variable > 0:
            sum_digits += help_variable % 10
            help_variable = int(help_variable / 10)
    if sum_digits in special:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
