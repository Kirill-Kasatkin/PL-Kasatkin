"""Вариант 1"""


"""Задание 1"""


import math

def square_rectangle(a, b):      #Площадь прямоугольника
    return a * b
def square_triangle(base, height):         #Площадь треугольника
    return 0.5 * base * height
def square_circle(radius):               #Площадь круга
    return math.pi * radius**2
def square_square(side):         #Площадь квадрата
    return side**2
def square_polygon(side, radius, corners):       #Площадь многоугольника
    return (1/2)*corners*side*radius
def square():       #Пользователь выбирает, какая ему нужна фигура, а затем по ней вводит данные
    print("Выберите фигуру:")
    print("1. Прямоугольник")
    print("2. Треугольник")
    print("3. Круг")
    print("4. Квадрат")
    print("5. Правильный многоугольник")
    
    choice = input("Введите номер фигуры: ")

    if choice == "1":
        a = float(input("Введите длину прямоугольника: "))
        b = float(input("Введите ширину прямоугольника: "))
        print("Площадь прямоугольника:", square_rectangle(a, b))
    elif choice == "2":
        base = float(input("Введите основание треугольника: "))
        height = float(input("Введите высоту треугольника: "))
        print("Площадь треугольника:", square_triangle(base, height))
    elif choice == "3":
        radius = float(input("Введите радиус круга: "))
        print("Площадь круга:", square_circle(radius))
    elif choice == "4":
        side = float(input("Введите длину стороны квадрата: "))
        print("Площадь квадрата:", square_square(side))
    elif choice == "5":
        side = float(input("Введите кол-во сторон многоугольника: "))
        radius = float(input("Введите радиус многоугольника: "))
        corners = float(input("Введите кол-во углов многоугольника: "))
        print("Площадь многоуольника:", square_polygon(side, radius, corners))
    else:
        print("Неверный выбор фигуры!")

square()

"""Задание 2"""


def calculate_sum(array):
    return sum(array)
def calculate_average(array):
    return sum(array) / len(array)
def calculate_statistics():
    arrays = []
    for i in range(3):
        array = []
        size = int(input(f"Введите размер массива {i+1}: "))
        for j in range(size):
            element = int(input(f"Введите элемент {j+1} массива {i+1}: "))
            array.append(element)

        arrays.append(array)

    for i, array in enumerate(arrays):
        print(f"Массив {i+1}:")
        print("Сумма элементов:", calculate_sum(array))
        print("Среднее арифметическое значение:", calculate_average(array))
        print()

calculate_statistics()



"""Вариант 10"""




"""Задание 1"""
def Y(a, b, c, n):
    spisok = [4, 2, 7, 9, 6, 3]  # список из цифр
    count = 0
    for n1 in spisok:  # каждая цифра должна побывать на 1-м месте
        for n2 in spisok:  # каждая цифра должна побывать на 2-м месте
            for n3 in spisok:  # каждая цифра должна побывать на 3-м месте
                x = n3 * 100 + n2 * 10 + n1  # воспроизводим число
                if x >= 100 and x <= n:  # проверяем
                    count += 1
    return count

print(Y(1, 2, 3, 900))

"""Задание 2"""
def REVERSE(str):
    word = str.split()  # Разбиваем строку на слова
    str_reverse  = ' '.join(reversed(word)) # Переворачиваем порядок слов и объединяем их обратно
    return str_reverse

stroka = input('Введите строку:')
result = REVERSE(stroka) # Вызов ф-ции и вывод результата
print('Результат:', result)