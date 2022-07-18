number = input()
number_length = len(number)
happy_year = int(number)

while True:
    happy_year += 1
    number_in_set = set(str(happy_year))
    set_length = len(number_in_set)
    if number_length == set_length:
        break


print(happy_year)
