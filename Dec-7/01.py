
word = input('Введите слово любой длины: ')
code = [ord(char) for char in word]

sum = 0
for x in code:
    sum += x 
print(f'Сумма кодов символов в вашем слове равна {sum}') 