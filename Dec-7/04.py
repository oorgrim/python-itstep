
user_length = input("Введите длину строки: ")
c1 = input("Введите первый символ: ")
c2 = input("Введите второй символ: ")

try:
    n = int(user_length)

except:
    print('Введите корректные данные!')

else:
    result = ''
    for x in range(n):
        if x % 2 == 0:
            result += c1
        else:
            result += c2
    print(f"Строка из добавленных ваши символов: {result}")