
user_data = input("Введите общую сумму продаж за месяц: ")

try:
    sales_amount = float(user_data)
except ValueError:
    print("Введите число! (вы ввели символ)")
else:
    salary = 250 + 0.10 * sales_amount
    print("Зарплата работника составит: ", salary)