user_data1 = input("Введите a: ")
user_data2 = input("Введите b: ")

try:
    a, b = int(user_data1), int(user_data2)
except ValueError:
    print("Введите число! (вы ввели символ)")
else:
    x = -b / a
    print("x равен ", x)