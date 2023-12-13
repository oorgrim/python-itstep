
user_data = input("Введите год: ")

try:
    year = int(user_data)
except ValueError:
    print("Введите число (год)")
else:
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        print(year, "год - високосный.")
    else:
        print(year, "год - не високосный.")