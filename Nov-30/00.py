
try:
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    #VN:     ^^^^^^^ разделяйте получение данных и преобразование
    # т.е. не делайте input и преобразование в int в одной строке
    # Это относится и к остальным вашим программам
except ValueError:
    print('введите число!')


else:
    result = 0

    current_number = start
    while current_number <= end:
        result += current_number
        current_number += 1

    print(f"Сумма чисел в диапазоне от {start} до {end} = {result}")