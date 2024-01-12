
import random

def play_guess(secret, attempts):
    print("Угадайте число от 1 до 100!!")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Попытка #{attempt}. Введите ваше число: "))

        if guess == secret:
            print(f"Поздравляю! Вы угадали число за {attempt} попыток")
            return attempt
        elif guess < secret:
            print("Загаданное число больше вашего")
        else:
            print("Загаданное число меньше вашего")

    print(f"Вы не смогли угадать. А число было: {secret}.")
    return attempts

secret_number = random.randint(1, 100)
attempts_limit = 5
result_attempts = play_guess(secret_number, attempts_limit)