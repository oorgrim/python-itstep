import math
user_data1 = input("Введите длину окружности: ")
user_data2 = input("Введите периметр квадрата: ")
try:
    length = float(user_data1)
    square_perimeter = float(user_data2)
    
    radius = length / (2 * math.pi)
    square_side = square_perimeter / 4
    
    circle_area = math.pi* (radius ** 2)
    square_area = square_side** 2
    
    if circle_area <= square_area:
        print("Окружность может поместиться внутри указанного квадрата ")
    else:
        print("Окружность не поместится внутри указанного квадрата")
        
except ValueError:
    print("Ошибка: Введите числовые значения для длины окружности и периметра квадрата.")
