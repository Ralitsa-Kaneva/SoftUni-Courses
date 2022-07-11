hour = int(input())
minutes = int(input())
timeAfter15Minutes = 0

if minutes + 15 >= 60:
    minutes += 15 - 60
    hour += 1
    if hour == 24:
        hour = 0
else:
    minutes += 15

if minutes < 10:
    print(f'{hour}:0{minutes}')
else:
    print(f'{hour}:{minutes}')

