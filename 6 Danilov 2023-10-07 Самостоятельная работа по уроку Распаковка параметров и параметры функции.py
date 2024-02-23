"""
https://urban-university.ru/members/courses/course999421818026/20231007-0000samostoatelnaa-rabota-po-uroku-raspakovka-parametrov-i-parametry-funkcii-495057292756

ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/10/07 00:00|Самостоятельная работа по уроку "Распаковка параметров и параметры функции"
Домашнее задание по уроку "Распаковка параметров и параметры функции"

Цель задания:
Освоить создание функций с параметрами по умолчанию и практику вызова этих функций с различным количеством аргументов.

Задание:


Функция с параметрами по умолчанию:
Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
Функция должна выводить эти параметры.
Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])

Распаковка параметров:
Создайте список values_list с тремя элементами разных типов.
Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
Распаковка + отдельные параметры:
Создайте список values_list_2 с двумя элементами разных типов
Проверьте, работает ли print_params(*values_list_2, 42)

"""

def print_params(a = 5, b = 'winter', c = True):
    print('First argument:\t\t', a)
    print('Second argument:\t', b)
    print('Third argument:\t\t', c)
    return


print_params()
"""
Result 
First argument:		 5
Second argument:	 winter
Third argument:		 True
"""

print_params(100, 'summer',False)
"""
Result 
First argument:		 5
Second argument:	 winter
Third argument:		 True
First argument:		 100
Second argument:	 summer
Third argument:		 False
"""

print_params(a=66,c =False)

"""
Result 
First argument:		 5
Second argument:	 winter
Third argument:		 True
First argument:		 100
Second argument:	 summer
Third argument:		 False
First argument:		 66
Second argument:	 winter
Third argument:		 False
"""

print_params(b='fall')

"""
First argument:		 5
Second argument:	 winter
Third argument:		 True
First argument:		 100
Second argument:	 summer
Third argument:		 False
First argument:		 66
Second argument:	 winter
Third argument:		 False
First argument:		 5
Second argument:	 fall
Third argument:		 True
"""

values_list = [1001,'spring',None]
values_dict = {'a': 200, 'b': 'year','c': False}

print_params(*values_list)
print_params(**values_dict)

"""
First argument:		 5
Second argument:	 winter
Third argument:		 True
First argument:		 100
Second argument:	 summer
Third argument:		 False
First argument:		 66
Second argument:	 winter
Third argument:		 False
First argument:		 5
Second argument:	 fall
Third argument:		 True
First argument:		 1001
Second argument:	 spring
Third argument:		 None
First argument:		 200
Second argument:	 year
Third argument:		 False
"""

values_list_2 = [5, 'wrong']
print_params(*values_list_2)

"""
First argument:		 5
Second argument:	 winter
Third argument:		 True
First argument:		 100
Second argument:	 summer
Third argument:		 False
First argument:		 66
Second argument:	 winter
Third argument:		 False
First argument:		 5
Second argument:	 fall
Third argument:		 True
First argument:		 1001
Second argument:	 spring
Third argument:		 None
First argument:		 200
Second argument:	 year
Third argument:		 False
First argument:		 5
Second argument:	 wrong
Third argument:		 True
"""

values_list_2 = [25, 'decade']
print_params(*values_list_2)

"""
First argument:		 5
Second argument:	 winter
Third argument:		 True
First argument:		 100
Second argument:	 summer
Third argument:		 False
First argument:		 66
Second argument:	 winter
Third argument:		 False
First argument:		 5
Second argument:	 fall
Third argument:		 True
First argument:		 1001
Second argument:	 spring
Third argument:		 None
First argument:		 200
Second argument:	 year
Third argument:		 False
First argument:		 5
Second argument:	 wrong
Third argument:		 True
First argument:		 25
Second argument:	 decade
Third argument:		 True
"""

print_params(*values_list_2, c = 'non boolean')

"""
First argument:		 5
Second argument:	 winter
Third argument:		 True
First argument:		 100
Second argument:	 summer
Third argument:		 False
First argument:		 66
Second argument:	 winter
Third argument:		 False
First argument:		 5
Second argument:	 fall
Third argument:		 True
First argument:		 1001
Second argument:	 spring
Third argument:		 None
First argument:		 200
Second argument:	 year
Third argument:		 False
First argument:		 5
Second argument:	 wrong
Third argument:		 True
First argument:		 25
Second argument:	 decade
Third argument:		 True
First argument:		 25
Second argument:	 decade
Third argument:		 non boolean
"""