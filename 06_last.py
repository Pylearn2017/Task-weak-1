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

num = int(input())
answer = num % 10
print(answer)
input()