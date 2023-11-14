"""Вариант 10"""


"""Задание 1"""
n = int(input())
a, b, c = input(), input(), input()

def chisla(a, b, c, N):
    count = 0
    for i in range(100, N + 1):
        digit = str(i)
        if a in digit and b in digit and c in digit:
            count += 1
    return count

print(chisla(a, b, c, n))



"""Задание 2"""
def REVERSE(stroka):
    word = stroka.split()
    str_reverse  = ' '.join(reversed(word)) 
    return str_reverse

stroka = input('Введите строку:')
result = REVERSE(stroka) 
print('Результат:', result)
