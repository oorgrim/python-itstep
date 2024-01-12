while True:
    try:
        num = int(input('Введите число: '))
        break
    except ValueError:
        print('Введите корректное число!')

divisions_count = 0
while num > 50:
    num /= 2
    divisions_count += 1

print(f"Получившееся число: {num}\nБыло сделано {divisions_count} попыток.")