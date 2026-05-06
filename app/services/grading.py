def calculate_grade(marks: list[int]):
    avg = sum(marks) / len(marks)

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "F"

    return avg, grade