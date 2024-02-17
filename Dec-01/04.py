user_input = input("Введите число: ")

if user_input.isdigit():
    number = int(user_input)

    max_digit = 0
    min_digit = 9

    while number > 0:
        digit = number % 10
        if digit > max_digit:
            max_digit = digit
        if digit < min_digit:
            min_digit = digit
        number //= 10

    print(f"Наибольшая цифра в числе: {max_digit}")
    print(f"Наименьшая цифра в числе: {min_digit}")

else:
    print("Введите корректное число!")