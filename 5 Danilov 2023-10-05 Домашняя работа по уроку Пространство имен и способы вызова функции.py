"""
https://urban-university.ru/members/courses/course999421818026/20231005-0000domasnaa-rabota-po-uroku-prostranstvo-imen-i-sposoby-vyzova-funkcii-685635746697

ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/10/05 00:00|Домашняя работа по уроку "Пространство имен и способы вызова функции"
Домашнее задание по уроку "Пространство имен и способы вызова функции"
Для работы над домашнем заданием:
1. Создайте новый проект в PyCharm

Ваша задача в файле main.py:
Создайте новую функцию def test...
Создайте две переменные a и b внутри пространства имен функции test
Распечатайте a и b внутри функции test
Создайте функцию def test2 с тремя параметрами, функция должна распечатывать все три параметра внутри своего тела
В ответ прикрепите получившийся файл main.py
"""

def test():
    a_local_test = 500
    b_local_test = 800
    print(a_local_test,b_local_test)
    return

def test2():
    a_local_test2 = 5000
    b_local_test2 = 8000
    print(a_local_test2, b_local_test2)
    return

test()
test2()