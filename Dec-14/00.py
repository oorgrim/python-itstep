
user_data = input("Введите текст: ")

try:
    max_len = int(input("Введите максимальную длину строк в символах: "))

except ValueError:
    print("Введите число!")

else:
    sentences = user_data.split('. ')

    formatted_sentences = []
    for sentence in sentences:
        sentence = ' '.join(sentence.split())

        if sentence.startswith('\n'):
            sentence = '    ' + sentence[ 1:]

        sentence = sentence.capitalize()

        words = sentence.split()
        current_line = ''

        for word in words:
            if len(current_line) + len(word)+ 1 <= max_len: #проверка на превышение макс длины строки
                current_line += word + ' '
            else:
                formatted_sentences.append(current_line.rstrip())
                current_line = word + ' '
        formatted_sentences.append(current_line.rstrip())

    max_sentence_length = max(len(sentence) for sentence in formatted_sentences[:-1])
    formatted_text = ''

    for sentence in formatted_sentences[:-1]:
        padding = ' '* (max_sentence_length - len(sentence))
        formatted_text += sentence + padding + '\n'
    formatted_text += formatted_sentences[-1]

    print(f"Отформатированный текст: {formatted_text}")