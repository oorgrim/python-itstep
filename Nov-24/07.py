
score = 0

question1 = "Как расшифровывается HTML?"
options1 = ["HyperText Markup Language", "HighText Languahe", "HiddenText Language"]
correct_option1 = "HyperText Markup Language"

user_answer1 = input(f"{question1}\n 1. {options1[0]}\n 2. {options1[1]}\n 3. {options1[2]}\n Ваш ответ: ")

if user_answer1.lower() == correct_option1.lower():
    score += 2
    print("Правильно! +2 балла.")
else:
    print(f"Неправильно! Правильный ответ: {correct_option1}.")

question2 = "Какая столица Франции?"
options2 = ["Лондон", "Берлин", "Париж"]
correct_option2 = "Париж"

user_answer2 = input(f"{question2}\n1. {options2[0]}\n2. {options2[1]}\n3. {options2[2]}\nВаш ответ: ")

if user_answer2.lower() == correct_option2.lower():
    score += 2
    print("Правильно! +2 балла.")
else:
    print(f"Неправильно! Правильный ответ: {correct_option2}.")

question3 = "Кто создал ЯП Python?"
options3 = ["Расмус Лердорф", "Ларри Уолл", "Гвидо ван Россум"]
correct_option3 = "Гвидо ван Россум"

user_answer3 = input(f"{question3}\n1. {options3[0]}\n2. {options3[1]}\n3. {options3[2]}\nВаш ответ: ")

if user_answer3.lower() == correct_option3.lower():
    score += 2
    print("Правильно! +2 балла.")
else:
    print(f"Неправильно! Правильный ответ: {correct_option3}.")

print(f"Ваш итоговый балл: {score}.")
