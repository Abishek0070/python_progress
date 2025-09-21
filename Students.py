students = [
    {
        "name": "Alice",
        "scores": [85, 92, 78]
    },
    {
        "name": "Bob",
        "scores": [70, 65, 88, 75]
    },
    {
        "name": "Charlie",
        "scores": [95, 100, 92, 98]
    }
]


for student in students:

    name = student["name"]
    scores = student["scores"]

    average_score = sum(scores) / len(scores)

    if average_score >= 90:
        grade = "A"
    elif average_score >= 80:
        grade = "B"
    elif average_score >= 70:
        grade = "C"
    elif average_score >= 60:
        grade = "D"
    else:
        grade = "F"

    
    print(f"{name}'s average score is {average_score:.2f} and their final grade is {grade}")