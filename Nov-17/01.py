user_data1 = input("Введите ускорение: ")
user_data2 = input("Введите скорость: ")
user_data3 = input("Введите время: ")

a, v, t = float(user_data1), float(user_data2), float(user_data3)

s = v * t + (a * t**2) / 2

print("Расстояние будет равно ", s)