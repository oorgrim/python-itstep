days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
current_day_ind = 0

while True:
    user_input = input(f'День недели - {days[current_day_ind]}, хотите увидеть следующий день? (Введите "OK" для продолжения) ')
    
    if user_input.lower() == 'ok':
        current_day_ind = (current_day_ind + 1) % len(days)
    else:
        break
