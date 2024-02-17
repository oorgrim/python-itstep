user_input = input("Введите число: ")
num = int(user_input)

def get_divisors(num):
    divisors = []
    for x in range(1, num + 1):
        if num % x == 0:
            divisors.append(x)
    return divisors

divisors = get_divisors(num)
print(f"Делители числа {num}: {divisors}")