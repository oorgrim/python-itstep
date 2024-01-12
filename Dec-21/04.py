# <<<<<<< HEAD
# =======

def is_perfect_number(number):

    if number <= 0:
        return False
    divisors = [i for i in range(1, number) if number % i == 0]
    sum_of_divisors = sum(divisors)
    return sum_of_divisors == number
    #VN: класс!! ^^^^^^^^^^^^^^^ особенно вот это. очень изящно получилось

try:
    input_number = int(input('Введите число для проверки: '))

except ValueError:
    print('Некорректные данные!')

else:
    if is_perfect_number(input_number):
        print(f"{input_number} - совершенное число")
    else:
        print(f"{input_number} - не совершенное число")
# >>>>>>> 02a690937efb5cd804fc4a2b3540c5097144403d
