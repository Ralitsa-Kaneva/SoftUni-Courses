import math

currentWorldRecordSeconds = float(input())
distanceMeters = float(input())
timeSecondsFor1m = float(input())
delayTimes = distanceMeters // 50
delay = delayTimes * 30

georgeTime = distanceMeters * timeSecondsFor1m + delay

if georgeTime < currentWorldRecordSeconds:
    print(f'Yes! The new record is {georgeTime:.2f} seconds.')
else:
    print(f'No! He was {georgeTime - currentWorldRecordSeconds:.2f} seconds slower.')