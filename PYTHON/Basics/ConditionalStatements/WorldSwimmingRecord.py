import math

currentWorldRecord = float(input())
distance = float(input())
timeFor1m = float(input())
delayTimes = distance // 15
delay = delayTimes * 12.5

ivansTime = distance * timeFor1m + delay

if ivansTime < currentWorldRecord:
    print(f'Yes, he succeeded! The new world record is {ivansTime:.2f} seconds.')
else:
    print(f'No, he failed! He was {ivansTime - currentWorldRecord:.2f} seconds slower.')
