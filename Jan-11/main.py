import employee_module as emp_mod

new_employee_res = emp_mod.newEmployee("Сабина Кункаева", "01.01.2000", "Бизнесмен", 500000)
print(new_employee_res)

new_employee_res = emp_mod.newEmployee("Кан Эрик", "02.03.2002", "Менеджер", 600000)
print(new_employee_res)

fire_employee_res = emp_mod.fireEmployee(1)
print(fire_employee_res)

employeeId = emp_mod.getEmployeeId("Эрик")
print(f"ID сотрудника: {employeeId}")

employeeRecord = emp_mod.getEmployeeRecord(employeeId)
print(employeeRecord)

fired_employees = emp_mod.getFiredEmployees()
print("Уволенные сотрудники:")
for employee in fired_employees:
    print(employee)

total_salary = emp_mod.getTotalSalary()
min_salary, max_salary, avg_salary, median_salary = emp_mod.getMinMaxAvgSalary()

print(f"Общий размер зарплатного фонда компании: {total_salary}")
print(f"Минимальная зарплата: {min_salary}")
print(f"Максимальная зарплата: {max_salary}")
print(f"Средняя зарплата: {avg_salary}")
print(f"Медианная зарплата: {median_salary}")