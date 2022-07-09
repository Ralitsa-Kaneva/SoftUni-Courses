deposite_sum = float(input())
deposite_deadline = int(input())
annual_rate_percent = float(input())
annual_rate_for_one_month = (deposite_sum*annual_rate_percent / 100)/12
rate = deposite_deadline * annual_rate_for_one_month
total_sum = deposite_sum + rate

print (f'{total_sum :.2f}')