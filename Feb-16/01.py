"""Генератор случайных чисел: Создайте генератор, который
генерирует случайные числа в диапазоне."""

import random
def generate_rand_num(start, end, count):
    start = int(input("Введите минимальное число диапазона: "))
    end = int(input("Введите максимальное число диапазона: "))
    for _ in range(count):
        yield random.randint(start, end)

start = 1
end = 10
number_count = 5

random_numbers = generate_rand_num(start, end, number_count)

for number in random_numbers:
    print(number)
