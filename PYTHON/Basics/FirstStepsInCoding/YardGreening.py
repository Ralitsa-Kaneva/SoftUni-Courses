sq_m_for_greening = float(input())
total_price = sq_m_for_greening * 7.61
discount = (total_price*18)/100
needed_expenses = total_price - discount

print(f'The final price is: {needed_expenses :.2f} lv.')
print(f'The discount is: {discount} lv.')