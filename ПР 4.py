#Задание 1
a = int(input("Введите число: "))
b = int(input("Введите число: "))

while a <= b:
    print(a)
    a += 1

#Задание 2
n = int(input("Введите число: "))

summ = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    summ += fact
print(summ)

#Задание 3
a = int(input("Введите число: "))
b = int(input("Введите число: "))

for i in range(a, b + 1, -1):
    if i % 2 != 0:
        print(i)