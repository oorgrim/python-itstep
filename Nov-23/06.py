
user_data = int(input("Введите пятизначное число: "))
#VN:        ^^^^ похоже, это преобразование тут забыли убрать, т.к. оно теперь есть в try
try:
    num = int(user_data)
except ValueError:
    print("Введите число! (вы ввели символ)")
else:
    new_num = (num % 10) * 10000 + num // 10
    print("Результат : ", new_num)