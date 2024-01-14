
#это код с предыдущего задания, второе начинается с 74 строки 
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




# то что я добавила :
def getFiredEmployees():

    fired_employees = []  
    for employee in employees_db:
        if employee['firedDate'] is not None:
            fired_employees.append(employee)
    return fired_employees

def getTotalSalary():
    total_salary = 0  
    for employee in employees_db:
        if employee['firedDate'] is None:
            total_salary += employee['salary']
    return total_salary

def getMinMaxAvgSalary():

    active_salaries = []  
    for employee in employees_db:
        if employee['firedDate'] is None:
            active_salaries.append(employee['salary'])

    if not active_salaries: #если нет сотруднкиков ( активных , либо вовсе их нет)
        return None, None, None, None
    
    sorted_salaries = sorted(active_salaries) #сортировка списка зарплат
    # находим мин и макс зарплату
    min_salary = sorted_salaries[0]
    max_salary = sorted_salaries[-1]
    avg_salary = sum(active_salaries) / len(active_salaries) #средняя
    
    n = len(sorted_salaries) #мндиана
    if n % 2 == 0:
        median_salary = (sorted_salaries[n // 2 - 1] + sorted_salaries[n // 2]) / 2
    else:
        median_salary = sorted_salaries[n // 2]
    
    return min_salary, max_salary, avg_salary, median_salary
    #VN: выражение n // 2 встречается часто, поэтому лучше вычислить его заранее: half = n // 2


fired_employees = getFiredEmployees()
print("Уволенные сотрудники:")
for employee in fired_employees:
    print(employee)

total_salary = getTotalSalary()
min_salary, max_salary, avg_salary, median_salary = getMinMaxAvgSalary()

print(f"Общий размер зарплатного фонда компании: {total_salary}")
print(f"Минимальная зарплата: {min_salary}")
print(f"Максимальная зарплата: {max_salary}")
print(f"Средняя зарплата: {avg_salary}")
print(f"Медианная зарплата: {median_salary}")