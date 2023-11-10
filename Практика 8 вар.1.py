"""Вариант 1"""

"""Задание 1"""
import random

N = 5  # размерность матрицы
# создание матрицы и заполнение случайными числами
A = [[random.randint(-10, 10) for j in range(N)] for i in range(N)]
# вывод матрицы
print("Матрица A:")
for i in range(N):
    for j in range(N):
        print(A[i][j], end=" ")
    print()

# вычисление суммы и количества положительных элементов над главной диагональю
sum_pol = 0
count_pol = 0
for i in range(N):
    for j in range(i + 1, N):
        if A[i][j] > 0:
            sum_pol += A[i][j]
            count_pol += 1

# вывод результата
print("Сумма положительных элементов над главной диагональю:", sum_pol)
print("Количество положительных элементов над главной диагональю:", count_pol)








"""Задание 2"""
import random

N = 5  # количество строк матрицы
M = 4  # количество столбцов матрицы
# создание матрицы и заполнение случайными числами
B = [[random.randint(-10, 10) for j in range(M)] for i in range(N)]
# вывод матрицы
print("Матрица B:")
for i in range(N):
    for j in range(M):
        print(B[i][j], end=" ")
    print()

# обработка каждой строки матрицы
for i in range(N):
    # нахождение максимального и минимального элементов в строке
    max_element = max(B[i])
    min_element = min(B[i])

    # нахождение индексов максимального и минимального элементов в строке
    max_index = B[i].index(max_element)
    min_index = B[i].index(min_element)

    # обмен максимального элемента с первым элементом строки
    B[i][0], B[i][max_index] = B[i][max_index], B[i][0]

    # обмен минимального элемента с последним элементом строки
    B[i][-1], B[i][min_index] = B[i][min_index], B[i][-1]

# вывод результата
print("Измененная матрица B:")
for i in range(N):
    for j in range(M):
        print(B[i][j], end=" ")
    print()
