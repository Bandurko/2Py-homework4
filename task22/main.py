# Задача 22: Даны два неупорядоченных набора целых 
# чисел (может быть, с повторениями). Выдать без 
# повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит в строку первый список затем 
# на следующией строке второй список.

n = set (map(int, input('Введите первый список значений через пробел: ').split()))
m = set (map(int, input('Введите второй список значений через пробел: ').split()))

print (*n.intersection(m))