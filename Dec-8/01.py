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

tmp = nums[changed_first]
nums[changed_first] =  nums[changed_second]
nums[changed_second] = tmp
print(nums) 