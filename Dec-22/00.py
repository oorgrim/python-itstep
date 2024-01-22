
employees_db = []

def generate_id(): #генеиировать айди
    if not employees_db:
        return 1
    else:
        return max(employee['id'] for employee in employees_db) + 1

def newEmployee(fullName, birthDate, position, salary): #новый сотрудник  

    names = fullName.split()
    if len(names) != 2:
        return {'id': -1, 'errorDescription': 'Неверный формат полного имени'}

    employee = { #новый сотрудник
        'id': generate_id(),
        'firstName': names[0],
        'lastName': names[1],
        'birthDate': birthDate,
        'hiredDate': None,
        'firedDate': None,
        'position': position,
        'salary': salary
    }

    employees_db.append(employee)

    return {'id': employee['id'], 'errorDescription': None}

def fireEmployee(employee_id): #увольнение
    for employee in employees_db:
        if employee['id'] == employee_id:
            if employee['firedDate'] is not None:
                return {'id': -1, 'errorDescription': 'Сотрудник уже уволне!'}
            
            employee['firedDate'] = 'Сегодня'
            return {'id': employee_id, 'errorDescription': None}

    return {'id': -1, 'errorDescription': 'Сотрудник с указанным id не найден'}

def getEmployeeId(name): #найти сотрудника по ФИ
    for employee in employees_db:
        if name.lower() in [employee['firstName'].lower(), employee['lastName'].lower()]:
            #VN:        ^^^^^^^^^^^^^^^^^^^^ очень хороший подход, здорово!
            return employee['id']
    return -1

def getEmployeeRecord(employee_id):
    for employee in employees_db:
        if employee['id'] == employee_id:
            return employee
    return {'id': -1, 'errorDescription': 'Сотрудник с указанным id не найден'}

new_employee_res = newEmployee("Сабина Кункаева", "01.01.2000", "Бизнесмен", 500000)
print(new_employee_res)

new_employee_res = newEmployee("Кан Эрик", "02.03.2002", "Менеджер", 600000)
print(new_employee_res)

fire_employee_res = fireEmployee(1)
print(fire_employee_res)

employeeId = getEmployeeId("Эрик")
print(f"ID сотрудника: {employeeId}")

employeeRecord = getEmployeeRecord(employeeId)
print(employeeRecord)