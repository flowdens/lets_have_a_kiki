# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def divide(a, b):
    return a / b if b != 0 else None


n, m = map(int, input("Введите два числа через пробел\n").split(" "))
res = divide(n, m)
print(res)

# 2. Выполнить функцию, которая принимает несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def print_person_info(name, birth_year, city, email, tel):
    print(name, birth_year, city, email, tel)


print_person_info(
    birth_year=1993,
    city="Manchester",
    name='Emilia',
    tel='89998883344',
    email='emlo@gmail.com')

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    if a < b and a < c:
        return b + c
    elif b < a and b < c:
        return a + c
    else:
        return a + b

print(my_func(1,2,3))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# 1
def my_func(x, y):
    return x ** y

# 2
def my_func(x, y):
    r = 1
    for i in range(y):
        r *= x
    return r


n1, n2 = map(int, input().split())
print(my_func(n1, n2))


# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.

s = 0
run = True

while run:
    args = input().split(" ")
    for d in args:
        if '#' == d:
            run = False
            break
        s += int(d)
    print(s)

# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
# и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def int_func(strk):
    return strk[:1].upper() + strk[1:]


print(int_func('text'))


# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def wrapper_dunc(line):
    r = ''
    for word in line.split(" "):
        r += int_func(word) + ' '
    return r

print(wrapper_dunc('text ulala viola davis'))
