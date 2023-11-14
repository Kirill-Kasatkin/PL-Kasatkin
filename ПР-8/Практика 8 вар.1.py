"""Вариант 1"""

"""Задание 1"""
import random

n = 5

A = []
for i in range(n):
    B = []
    for i in range(n):
        B.append(random.randint(-9, 9))
    A.append(B)

for row in A:
    for elem in row:
        print(elem, end=' ')
    print()

summa = 0
count = 0

for i in range(n):
    for j in range(i + 1, n):
        if A[i][j] > 0:
            summa += A[i][j]
            count += 1

print("Сумма положительных чисел:", summa)
print("Количество положительных чисел:", count)




"""Задание 2"""
import random

N = 5
M = 4
B = []

for i in range(N):
    A = []
    for i in range(M):
        A.append(random.randint(-9, 9))
    B.append(A)
print("Начальная матрица B:")

for row in B:
    for elem in row:
        print(elem, end=' ')
    print()

for i in range(N):
    max_elem = max(B[i])
    min_elem = min(B[i])

    max_index = B[i].index(max_elem)
    min_index = B[i].index(min_elem)

    B[i][0] = B[i][max_index]
    B[i][max_index] = B[i][0]
    B[i][-1] = B[i][min_index]
    B[i][min_index] = B[i][-1]

print("Измененная матрица B:")
for row in B:
    for elem in row:
        print(elem, end=' ')
    print()