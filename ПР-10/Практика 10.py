import random

n = 5
A = []
for i in range(n):
    B = []
    for i in range(n):
        B.append(random.randint(-9, 9))
    A.append(B)

with open('C:\\Users\\DedKir\\Desktop\\Языки программировния\\Практика\\Касаткин_УБ-32_vvod.txt', 'w') as testfile:
    for row in A:
        testfile.write(' '.join([str(a) for a in row]) + '\n')


with open("C:\\Users\\DedKir\\Desktop\\Языки программировния\\Практика\\Касаткин_УБ-32_vivod.txt", "w") as vivod:

    summa = 0
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if A[i][j] > 0:
                summa += A[i][j]
                count += 1

    vivod.write("Сумма положительных чисел:")
    vivod.write(' ')
    vivod.write(str(summa))
    vivod.write('\n')
    vivod.write("Количество положительных чисел:")
    vivod.write(' ')
    vivod.write(str(count))
