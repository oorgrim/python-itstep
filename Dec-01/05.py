user_input = input("Введите число: ")

if user_input.isdigit():
    number = user_input
    user_input_sdvig = input("На сколько цифр сдвинуть число (влево): ")
    sdvig = int(user_input_sdvig)
    
    for _ in range(sdvig):
        number = number[1:] + number[0]

    print(f"Исходное число: {user_input}")
    print(f"Результат сдвига на {sdvig} цифр влево: {number}")

else:
    print("Введите корректное число")