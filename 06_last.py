'''
Вводится единственное целое неотрицательное число.
Получить последнюю цифру

Примеры:

Тест 1
Входные данные:
179

Вывод программы:
9
'''

a = int(input('Введите любое число: '))
b = a // 10
d = b * 10
c = a - d
print(c)
input()
