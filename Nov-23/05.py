
user_data1 = input("Введите трехзначное число: ")


try:
    num = int(user_data1)
except ValueError:
    print("Введите число! (вы ввели символ)")
else:
    second_num = (num % 100) //10
    print("Вторая цифра введенного числа:", second_num)