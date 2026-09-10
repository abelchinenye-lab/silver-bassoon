
## Student Graging System
students = ["Obinna", "Adaeze", "Emeka", "Chibuzor", "Chinaza","Chikamso", "Chinenye", "Amaka", "Chika", "Ndidi","Ndubuisi", "Nzubechukwu", "Obiora", "Chinedu", "Uchenna"]
scores = [78, 87, 65, 57, 89, 97, 92, 83, 52, 89, 87, 90, 47, 71, 74]

total = 0

## For Loop
for student, score in zip(students, scores,):
    total += score
## Assigning Grades
    if score >= 85:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 65:
        grade = "C"
    elif score >= 55:
        grade = "D"
    elif score >= 45:
        grade = "E"
    else:
        grade = "F"
    print(student,"-", score,"-",grade)

## Average
average = total / len(scores)

## Display
print("Class Average is :", average)
