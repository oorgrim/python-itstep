from functools import reduce

students = [
    {'name': 'Alan Alanov', 'age': 23, 'course': 'Python', 'average_grade': 9.72},
    {'name': 'Alana Williams', 'age': 21, 'course': 'Java', 'average_grade': 9.91},
    {'name': 'Temirlan Ibrayev00', 'age': 17, 'course': 'C++', 'average_grade': 7.27}
]

total_age = reduce(lambda acc, x: acc + x['age'], students, 0)
average_age = total_age / len(students)
print("Средний возраст всех студентов:", average_age)

python_students = list(filter(lambda x: x['course'] == 'Python', students))
total_grade_python = reduce(lambda acc, x: acc + x['average_grade'], python_students, 0)
average_grade_python = total_grade_python / len(python_students)
print("Средний балл студентов на курсе 'Python':", average_grade_python)

