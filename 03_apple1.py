'''
N школьников делят K яблок поровну, не делящийся остаток остается в корзинке. 
Сколько яблок достанется каждому школьнику?

Примеры:

Тест 1
Входные данные:
3
14


Вывод программы:
4
'''
print('кол-во школьников')
a = input()
a = int(a)

print('кол-во яблок')
b = input()
b = int(b)

print(b // a)
input()