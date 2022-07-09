import math

pages_in_book = int(input())
pages_to_read_for_hour = int(input())
days_to_read_a_book = int(input())

needed_hours = pages_in_book / pages_to_read_for_hour

read_hours_daily = round(needed_hours / days_to_read_a_book,2)

print (read_hours_daily)