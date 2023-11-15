"""Вариант 4"""
import random

"""Задание 1"""
import random

N = 7
M = 5
A = []

for i in range(N):
    B = []
    for i in range(M):
        B.append(random.randint(0, 9))
    A.append(B)

print("Исходная матрица: ")
for row in A:
    for elem in row:
        print(elem, end=' ')
    print()
print()

summa = []

for row in A:
    summa.append(sum(row))
for i in range(N):
    if sum(A[i]) == max(summa):
        print(A[i], max(summa))
for i in range(N):
    if sum(A[i]) == min(summa):
        print(A[i], min(summa))



"""Задание 2"""

N = 3
A = []

for i in range(N):
    B = []
    for i in range(N):
        B.append(random.randint(-9, 9))
    A.append(B)

print("Исходная матрица: ")
for row in A:
    for elem in row:
        print(elem, end=' ')
    print()
print()

for i in range(N):
    for j in range(N):
        if A[i][j] > 0:
            A[i][j] = 1
        else:
            A[i][j] = 0

for row in A:
    for elem in row:
        print(elem, end=' ')
    print()

for i in range(len(A)):
    print(*[A[i][j] if j < i else ' ' for j in range(len(A[i]))], ' ')
print("ИЛИ")
for i in range(len(A)):
    print(*[A[i][j] if j <= i else ' ' for j in range(len(A[i]))], ' ')