actorName = input()
actorPoints = float(input())
judgesNumber = int(input())
judgePoints = 0
judgeNameLength = 0
actorPointsFromJudges = 0
nominated = False

for i in range(0, judgesNumber):
    judgeName = input()
    judgeNameLength = len(judgeName)
    judgePoints = float(input())
    actorPointsFromJudges = (judgeNameLength * judgePoints) / 2
    actorPoints += actorPointsFromJudges
    if actorPoints > 1250.5:
        nominated = True
        print(f'Congratulations, {actorName} got a nominee for leading role with {actorPoints:.1f}!')
        break
if actorPoints < 1250.5:
    print(f'Sorry, {actorName} you need {1250.5 - actorPoints:.1f} more!')


