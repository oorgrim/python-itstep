input_first_list = input('Введите элементы для первого списка: ')  
input_second_list = input('Введите элементы для второго списка: ')
first_list_split = input_first_list.split()
second_list_split = input_second_list.split()

first_list = []
second_list = []

for elem in first_list_split:
    first_list.append(elem)

for elem in second_list_split:
    second_list.append(elem)

res = []
for elem in first_list:
    if elem in second_list:
        res.append(elem)
if res:
    print("Совпадающие элементы: ", res)
else:
    print('Таковых нет')