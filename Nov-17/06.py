
user_data = int(input("Введите пятизначное число: "))
num = int(user_data)

new_num = (num % 10) * 10000 + num // 10

print("Результат : ", new_num)