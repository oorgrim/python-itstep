
try:
    fd = open("input03.txt", encoding="utf8")
except FileNotFoundError:
    print("Файл не найден!")
    exit()

lines = fd.readlines()
fd.close()

converted_lines = []

for line in lines:
    converted_words = []
    words = line.split()

    i = 0
    while i < len(words):
        word = words[i]

        if word.replace('.', '', 1).isdigit():
            currency = words[i + 1]
            exchange_rate = {'$': 432.5, 'USD': 432.5, '€': 509.2, 'EUR': 509.2}.get(currency, 1)
            converted_words.append(f'{float(word) * exchange_rate} ₸')
            i += 1
        else:
            converted_words.append(word)
            i += 1

    converted_lines.append(' '.join(converted_words))
try:
    with open("output03.txt", "w", encoding="utf8") as output_file:
        for line in converted_lines:
            output_file.write(line + '\n')
except FileNotFoundError:
    print("Файл не найден!")
except PermissionError:
    print("Здесь нельзя создавать файл")
