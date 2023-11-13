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
def REVERSE(stroka):
    word = stroka.split()
    print(word) # Разбиваем строку на слова
    str_reverse  = ' '.join(reversed(word))
    print(str_reverse) # Переворачиваем порядок слов и объединяем их обратно
    return str_reverse

stroka = input('Введите строку:')
result = REVERSE(stroka) # Вызов ф-ции и вывод результата
print('Результат:', result)
