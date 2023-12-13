word = input("Введите слово из пяти букв: ")

if len(word) != 5:
    print("ВВедите слово из ПЯТИ букв:")
else:
    if word == word[::-1]:
        print(word, "  - это палиндром")
    else:
        print(word, "- это не палиндром") 