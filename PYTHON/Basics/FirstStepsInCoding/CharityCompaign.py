campaign_days = int(input())
sweet_makers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

total_sum = (sweet_makers* ((cakes * 45) + (waffles * 5.8) + (pancakes * 3.2)))*campaign_days
expenses = total_sum / 8
total_sum_after_expenses = total_sum - expenses

print(round(total_sum_after_expenses,2))