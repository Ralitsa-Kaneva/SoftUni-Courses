firstRunSeconds=int(input())
secondRunSeconds=int(input())
thirdRunSeconds=int(input())

sumSeconds = firstRunSeconds + secondRunSeconds + thirdRunSeconds
minutes = sumSeconds // 60
seconds = sumSeconds % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')