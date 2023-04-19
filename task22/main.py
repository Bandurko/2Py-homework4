# Задача 22: Даны два неупорядоченных набора целых 
# чисел (может быть, с повторениями). Выдать без 
# повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит в строку первый список затем 
# на следующией строке второй список.

# Доп. материалы, которые мне помогли:
# https://all-python.ru/osnovy/mnozhestva.html
# https://proproprogs.ru/python_base/sortirovka-sort-i-sorted

# n = set(map(int, input('Введите первый список значений через пробел: ').split()))
# m = set(map(int, input('Введите второй список значений через пробел: ').split()))

from random import randint

len_n = int(input('Введите длину первого списка: '))
n = set(randint(1, 100) for i in range(len_n))
# print(n)
len_m = int(input('Введите длину второго списка: '))
m = set(randint(1, 100) for i in range(len_m))
# print(m)
print (*sorted(n.intersection(m)))