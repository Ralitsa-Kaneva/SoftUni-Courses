def abs_numbers():
    abs_list = []
    for number in my_list:
        current_number = abs(float(number))
        abs_list.append(current_number)
    return abs_list


my_list = input().split(" ")

print(abs_numbers())
