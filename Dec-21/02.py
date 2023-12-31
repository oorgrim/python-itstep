
def time_to_seconds(hours, minutes, seconds):

    if not (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59):
        print('некорректное значение времени!')
        exit()
    total_seconds = hours * 3600 + minutes * 60 + seconds

    return total_seconds

try:
    hours = int(input('Введите часы: '))
    minutes = int(input('Введите минуты: '))
    seconds = int(input('Введите секунды: '))

except ValueError:
    print('Некорректные данные!')

else:
    total_seconds = time_to_seconds(hours, minutes, seconds)
    print(f"Время в секундах: {total_seconds} секунд")