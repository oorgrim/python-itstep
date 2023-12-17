
year = input('Введите год: ')
month = input('Введите месяц: ')
day = input('Введите день: ')

if not year or not month or not day:
    print("Вы ничего не ввели.")
else:
    words = "%s.%s.%s"
    res = words % (day, month, year)
    print(res)