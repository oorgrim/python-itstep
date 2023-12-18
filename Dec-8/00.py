input_number = input('Введите числа: ')
input_number_list = input_number.split()
nums = []

for num_str in input_number_list:
    try:
        num = int(num_str)
        nums.append(num)
    except ValueError:
        print(f'{num_str} не является числом. Пропускаю это значение')
print(f'Ваш список: {nums}')


for i in range(1, len(nums)) :
    num_after = nums[i]
    num_before = nums[i-1]
    if num_after > num_before:
        print(num_after)