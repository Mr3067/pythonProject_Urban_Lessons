""""
https://urban-university.ru/members/courses/course999421818026/20231014-0000domasnaa-rabota-po-uroku-moduli-i-pakety-775368892558

ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/10/14 00:00|Домашняя работа по уроку "Модули и пакеты"
Домашнее задание по уроку "Установка ipython и базовые структуры данных"

Создайте новый проект
Запустите новый проект в Pycharm

Ваша задача:
Создайте новый файл, в этом файле создайте две функции def, которые распечатывают "Hello, world"
В файле main.py импортируйте ранее созданный файл и вызовите две созданные ранее функции
Получившийся файл прикрепите к заданию.
Урок "Модули и пакеты"

"""
from pprint import pprint as newstyleprint


def stylePrint1(_str):
    newstyleprint(_str)
    return


def stylePrint2(_str):
    newstyleprint(_str)
    return

if __name__ == '__main__':
    a = 'Hello'
    b = ','
    c = 'World'
    e = 'Print from modul 8a'

    stylePrint1(a + b + c + e)
    stylePrint2(c + b + a + e)
    stylePrint1(a)