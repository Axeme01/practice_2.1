def calculate_average(grades):
    return sum(map(float, grades)) / len(grades)

with open('students.txt', 'w', encoding='utf-8') as file:
    lines = [
        'Иванов Иван:5, 4, 3, 5',
        'Петров Петр:4,3,4,4',
        'Сидорова Мария:5,5,5,5',
    ]

results = []
best_student = None
highest_avg = 0.0

for line in lines:
    name, grades_str = line.strip().split(':')
    grades = grades_str.split(',')

    avg_grade = calculate_average(grades)

    if avg_grade > 4.0:
        results.append((name, avg_grade))

    if avg_grade > highest_avg:
        best_student = name
        highest_avg = avg_grade

with open('result.txt', 'w') as output_file:
    for student, avg in results:
        output_file.write(f"{student}: {avg:.2f}\n")

if best_student is not None:
    print(f'Студент с наивысшим средним баллом: {best_student}, Средний балл: {highest_avg:.2f}')
else:
    print("Нет студентов с достаточным средним баллом.")