
input_employee = input("Введите имена сотрудников: ")
input_employee_list = input_employee.split()

employee_names = []

if not input_employee:
    print('Вы ничего не ввели!')
else:
    for employee in input_employee_list:
        employee_names.append(employee.capitalize()) #чтоыб программа работала с любым регистром (сначала привела все элементы в виде имен к одному регистру capitalize - она сделает заглавной только первую букву имени)
                                                     #VN: это хорошая практика!
    seen_names = set()
    duplicates = set()

    for name in employee_names:
        if name in seen_names:
            duplicates.add(name)
        else:
            seen_names.add(name)

    if duplicates:
        print("Следующие сотрудники получили премию дважды:")
        for name in duplicates:
            print(name)
    else:
        print("Нет сотрудников, которые получили премию дважды ")