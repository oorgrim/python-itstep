
input_nums = input('Введите числа: ')
input_nums_list = input_nums.split()

nums = []

for num_str in input_nums_list:
    try:
        num = int(num_str)
        nums.append(num)
    except:
        print(f'{num_str} не является числом. Пропускаю это значение')
print(f'Ваш список: {nums}')

        
max_num = max(nums)
min_num = min(nums)

changed_first = nums.index(max_num)
changed_second = nums.index(min_num)

difference = (changed_first - changed_second)-1
print(f"Расстояние между минимальным числом {min_num} и максимальным числом {max_num} равно {difference}")

"""VN: расстояние не может быть отрицательным. Также не нужно отнимать 1 при вычислении difference
Введите числа: 7 9 5 8 5 8
Ваш список: [7, 9, 5, 8, 5, 8]
Расстояние между минимальным числом 5 и максимальным числом 9 равно -2
"""