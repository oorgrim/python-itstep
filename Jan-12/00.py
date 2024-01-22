students = [
    {'name': 'Kira Yoshikage', 'age': 33, 'course': 'Python', 'average_grade': 7.12},
    {'name': 'Yagami Light', 'age': 18, 'course': 'Java', 'average_grade': 10},
    {'name': 'Alina Abdrakhmanova', 'age': 20, 'course': 'C++', 'average_grade': 8.1}
]

names = map(lambda student: student['name'], students)

print(tuple(names))