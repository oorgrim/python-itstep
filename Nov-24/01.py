user_data = input("Введите трехзначное число: ")
if len(user_data) != 3 or not user_data.isdigit():
    print("Пожалуйста, введите  трехзначное число правильно")
else:
    try:
        num1 = int(user_data[0])
        num2 = int(user_data[1])
        num3 = int(user_data[2])
    except ValueError:
        print("Пожалуйста, введите  трехзначное число правильно.")
    else:
        if num1 == num2 or num2 == num3 or num1 == num3:
            print("В числе есть одинаковые цифры")
        else:
            print("В числе нет одинаковых цифр")