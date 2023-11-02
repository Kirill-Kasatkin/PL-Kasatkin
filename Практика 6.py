"""Вариант 1"""



#Задание 1
n = int(input("Введите длину массива: ")) #Создание кол-ва чисел в массиве через клавиатуру
a = []
for i in range(n):
    print("Введите ", i, 'элемент')
    a.append(int(input())) #Добавление в список элементов, введённых через клавиатуру
print("Максимальный элемент списка: ", max(a))
a.reverse() #Разворачиваем список
print(a) #Вывод работы

#Задание 2
#Создаём функию, в которой всё будет просчитываться
def zero_elemets(n):
    summ = sum(n) #Сумма всех элементов списка
    zero_count = n.count(0) #Находим нули в списке
    average = summ / len(n) #Находим средее арифметическое всех чисел списка
    for i in range(len(n)): #Цикл по длине списка, чтобы находить те самые нули
        if lst[i] == 0:
            lst[i] = average #Заменяем нули на среднее арифметическое
    return n

lst = [1,0,67,4,7,2,5,0,0,0,6,4,3,6,7,2,5,8,5]
print(zero_elemets(lst)) #Вывод работы



"""Вариант 11"""


#Задание 1
m = list(map(int, input().split()))
a = []
for x in m:
    if (int(x))%2==0:
        a.append(x)
print(max(a))

#Задание 2
m = list(map(int, input().split()))
a = []
for x in m:
    if int(x)%2==0 and int(x)<10:
        a.append(x)
if len(a)==0:
    print('Таких чисел нет')
else:
    print(sorted(a))