'''
Напишите программу, которая приветствует пользователя, выводя слово Hello, введенное имя и знаки препинания по образцу 
(см. пример входных и выходных данных).
Программа должна считывать в строковую переменную значение и писать соответствующее приветствие.
Обратите внимание, что после запятой должен обязательно стоять пробел, а перед восклицательным знаком пробела нет.
Операцией конкатенации строк (+) пользоваться нельзя.

Примеры: 

Тест 1
Входные данные:
Harry

Вывод программы:
Hello, Harry!
'''


name = input()
print(f'Hello, {name}!')
input()
