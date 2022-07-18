def order():
    if product == "coffee":
        return quantity * 1.50
    if product == "water":
        return quantity * 1
    if product == "coke":
        return quantity * 1.40
    if product == "snacks":
        return quantity * 2


product = input()
quantity = int(input())

result = order()
print(f"{result:.2f}")
