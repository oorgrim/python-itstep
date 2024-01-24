students = [
    {'name': 'Marina', 'age': 31,'course': 'Python', 'average_grade': 12},
    #VN: пустые строки тут не нужно
    {'name': 'Melissa Kim', 'age': 17,'course': 'HTML', 'average_grade': 11},
    
    {'name': 'Aurora Smith', 'age': 22,'course': 'HTML', 'average_grade': 12},
    
    {'name': 'Andrey Cherkasov', 'age': 18,'course': 'Python', 'average_grade': 8},

    {'name': 'Sanzhar Ibrayev', 'age': 25,'course': 'HTML', 'average_grade': 10}
]

html_students = filter(lambda student: student['course'] == 'HTML', students)
print(f"\nКортеж студентов, только курса HTML: \n{list(html_students)}")

more_successful_students = filter(lambda student: student['average_grade'] > 11, students)
print(f'\nНаиболее преуспевающие ученики: \n{list(more_successful_students)}')