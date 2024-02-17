user_input  = input("Введите любое число: ")
num  = int(user_input)
counter = 0

while num != 1:
    if num % 2 == 0:
        new_num = num // 2
        counter += 1
    elif num % 2 == 1:
        new_num = (num * 3 + 1) // 2

    print(new_num)
    num = new_num
    counter += 1

print(f"количество итераций: {counter}")