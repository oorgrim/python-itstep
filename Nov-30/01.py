
try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
except ValueError:
    print('Введите число!')
else:
    while num2:
        num1, num2 = num2, num1 % num2
        
    print('Наибольший общий делитель: ', num1)