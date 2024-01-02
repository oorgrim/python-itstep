
positive_count = 0
negative_count = 0
zero_count = 0
even_count = 0
odd_count = 0

count = 0

while count < 10:
    try:
        number = int(input("Введите число: "))
    except ValueError:
        print('введите число!')
    else:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        count += 1



print(f"Положительных чисел: {positive_count}")
print(f"Отрицательных чисел: {negative_count}")
print(f"Нулей: {zero_count}")
print(f"Четных чисел: {even_count}")
print(f"Нечетных чисел: {odd_count}")
