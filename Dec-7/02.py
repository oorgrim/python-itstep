word = input('Введите слово: ')

short_name1 = word[:2]
short_name2 = word[-2:]

res = f"{short_name1}-{short_name2}"
print(res)