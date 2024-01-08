import random

try:
    N = int(input("Введите количество строк: "))
    M = int(input("Введите количество столбцов: "))
except ValueError:
    print('Введите число!')
else:
    if N <= 0 or M <= 0:
        print("Введите положительные числа!")
    else:
        matrix = [[random.randint(-20, 20) for x in range(M)] for x in range(N)]
        print("\nThe created matrix:")
        for row in matrix:
            print(' '.join(map(str, row)))  