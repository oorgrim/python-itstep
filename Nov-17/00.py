user_data = input("Введите десятичное число: ")

try:
    num = float(user_data)
    integer_num = int(num)
    binary = bin(integer_num)
    octal = oct(integer_num)
    hexadecimal = hex(integer_num)

except ValueError:
    print("Ошибка: введите корректное десятичное число.")
else: 
    print("Ваше число в двоичном виде:", binary)
    print("Ваше число в восьмеричном виде:", octal)
    print("Ваше число в шестнадцатеричном виде:", hexadecimal)