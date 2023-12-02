import math

user_data1 = input("Введите x-координату первой точки: ")
user_data2 = input("введите y-координату первой точки: ")
user_data3 = input("Введите x-координату второй точки: ")
user_data4 = input("введите y-координату второй точки: ")

try:
    y1 = float(user_data2)
    x1 = float(user_data1)

    x2 = float(user_data3)
    y2 = float(user_data4)
except ValueError:
    print("Введите число! (вы ввели символ)")
else:
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("Расстояние между точками = ", distance )