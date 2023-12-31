
def seconds_to_time(seconds):

    if seconds < 0:
        print("Отрицательное количество секунд не может быть")
        exit()

    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return time_string


try:
    input_seconds = int(input('Введите количество секунд: '))

except ValueError:
    print('Некорректные данные!')

else:
    formatted_time = seconds_to_time(input_seconds)
    print(f"Отформатированное время: {formatted_time}")