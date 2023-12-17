word = input('Введите слово: ')

if word:
    changed_word = chr(ord(word[0]) - ord('a') + ord('A')) + word[1:]
    print("Слово с большой буквы:", changed_word)
else:
    print("Вы ввели пустую строку.")