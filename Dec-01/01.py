user_input = input('Введите число: ')
num = int(user_input)

def get_fibonacci_sequence(n): #получить последоватеььность ФИбоначчи
    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < n:
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    return fibonacci_sequence

result = get_fibonacci_sequence(num)
print(result)
