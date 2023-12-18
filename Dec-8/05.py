
user_input = input('Введите что нибудь по типу гр@оо@лк@оц@ва: ')
result = ''

for char in user_input:
    if char == '@':
        result = result[:-1]
    else:
        result += char

print(result)