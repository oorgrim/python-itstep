
def is_perfect_number(number):

    if number <= 0:
        return False
    divisors = [i for i in range(1, number) if number % i == 0]
    sum_of_divisors = sum(divisors)
    return sum_of_divisors == number

def find_perfect_numbers_in_range(minimum, maximum):
    
    perfect_numbers = [num for num in range(minimum, maximum + 1) if is_perfect_number(num)]
    return perfect_numbers


try:
    min_range = int(input('Введите минимальное значение диапазона: '))
    max_range = int(input('Введите максимальное значение диапазона: '))

except ValueError:
    print('Некорректные данные!')

else:
    perfect_numbers_in_range = find_perfect_numbers_in_range(min_range, max_range)
    print(f"Совершенные числа в диапазоне от {min_range} - {max_range}: {perfect_numbers_in_range}")