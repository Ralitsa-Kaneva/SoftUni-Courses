def grade():
    if current_grade < 3:
        return "Fail"
    elif current_grade < 3.50:
        return "Poor"
    elif current_grade < 4.50:
        return "Good"
    elif current_grade < 5.50:
        return "Very Good"
    else:
        return "Excellent"


current_grade = float(input())

print(grade())
