def split_slogi(word):
    glasnye = "аеёиоуыэюяaeiouy"
    word = word.lower()

    def is_glasn(char):
        return char in glasnye

    slogi = []
    current_slog = ""

    for char in word:
        if is_glasn(char):
            current_slog += char
        else:
            if current_slog:
                slogi.append(current_slog)
                current_slog = ""
            current_slog += char

    if current_slog:
        slogi.append(current_slog)

    return "-".join(slogi)

try:
    with open("input04.txt", encoding="utf8") as input_file:
        word = input_file.read().strip()

    result = split_slogi(word)

    with open("output04.txt", "w", encoding="utf8") as output_file:
        output_file.write(result)

    print(f"Результат сохранен в файле output04.txt")

except FileNotFoundError:
    print("Файл не найден!")
except PermissionError:
    print("Здесь нельзя создавать файл")