user_input1 = input("Введите первое число: ")
user_input2 = input("Введите второе число: ")

try:
    num1 = int(user_input1)
    num2 = int(user_input2)
except ValueError:
    print("Ошибка, введите корректные числа")
    exit()

while True:
    sign = input("Какую арифметическую операцию вы хотите сделать? (введите знак +, -, /, *): ")

    match sign:
        case '+':
            res = num1 + num2
            print(f"Сумма чисел {num1} и {num2} равна {res}")
        case '-':
            res = num1 - num2
            print(f"Разность чисел {num1} и {num2} равна {res}")
        case '*':
            res = num1 * num2
            print(f"Произведение чисел {num1} и {num2} равно {res}")
        case '/':
            if num2 == 0:
                print("Ошибка: деление на ноль.")
            else:
                res = num1 / num2
                print(f"Деление чисел {num1} и {num2} равно {res}")
    
    continue_calculation = input("Хотите решить еще одну задачу? (введите 'yes' для продолжения): ")
    if not continue_calculation.lower().startswith('y'):
        print("Программа завершена")
        break