lines = int(input())
count = 0
sum_negatives = 0
list_of_positives = []
list_of_negatives = []

for i in range(lines):
    number = int(input())
    if number >= 0:
        count += 1
        list_of_positives.append(number)
    else:
        sum_negatives += number
        list_of_negatives.append(number)

print(f"{list_of_positives}\n{list_of_negatives}\nCount of positives: {count}\nSum of negatives: {sum_negatives}")
