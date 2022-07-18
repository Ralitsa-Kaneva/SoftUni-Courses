def rounding():
    my_list = []
    for num in numbers:
        current_num = round(float(num))
        my_list.append(current_num)
    return my_list


numbers = input().split(" ")

print(rounding())
