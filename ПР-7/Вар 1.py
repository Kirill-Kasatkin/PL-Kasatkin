"""Вариант 1"""


"""Задание 1"""
import math

def square_rectangle(a, b):     
    return a * b
def square_triangle(base, height):         
    return 0.5 * base * height
def square_circle(radius):             
    return math.pi * radius**2
def square_square(side):        
    return side**2
def square_polygon(side, radius, corners):       
    return (1/2)*corners*side*radius
def square():      
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
def summa(array):
    return sum(array)
def average_value(array):
    return sum(array) / len(array)
def function():
    arrays = []
    for i in range(3):
        array = []
        size = int(input(f"Введите размер массива {i+1} не больше 15: "))
        for j in range(size):
            element = int(input(f"Введите элемент {j+1} массива {i+1}: "))
            array.append(element)

        arrays.append(array)

    for i, array in enumerate(arrays):
        print(f"Массив {i+1}:")
        print("Сумма элементов:", sum(array))
        print("Среднее арифметическое значение:", average_value(array))
        print()

function()
