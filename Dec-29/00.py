def create_matrix(rows, cols):
    matrix = [[0] * cols for x in range(rows)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

try:
    N = int(input("Введите количество строк:  "))
    M = int(input("Введите количество столбцов: "))
except ValueError:
    print('Введите число!')
else:
    if N <= 0 or M <= 0:
        print("Введите пожалуйста положительные числа: ")
    else:
        matrix = create_matrix(N, M)
        print("Ваша матрица:")
        print_matrix(matrix)