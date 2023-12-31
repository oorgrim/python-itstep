
def format_time(hours, minutes=0, seconds=0):

    if not (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59):
        print("Некорректные значения времени.")
        #VN: функция не должна ничего печатать. Если функция называется format_time, это
        # значит, что она должна форматировать время и больше ничего
        exit()
        #VN: функция не должна решать, завершать программу или нет. Это просто функция.
        # побочные эффекты не делают функцию хорошей
    time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return time_string

try:
    hours = int(input('Введите часы: '))
    minutes = int(input('Введите минуты: '))
    seconds = int(input('Введ ите секунды: '))

except ValueError:
    print('Некорректные данные!')

else:
    formatted_time = format_time(hours, minutes, seconds)
    print(f"Отформатированнок время: {formatted_time}")