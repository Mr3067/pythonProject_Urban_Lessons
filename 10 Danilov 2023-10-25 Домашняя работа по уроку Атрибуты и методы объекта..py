"""
https://urban-university.ru/members/courses/course999421818026/20231025-0000domasnaa-rabota-po-uroku-atributy-i-metody-obekta-922879792642

ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/10/25 00:00|Домашняя работа по уроку "Атрибуты и методы объекта."
Домашнее задание по уроку "Пространство имен"

Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новый класс House
Задайте ему новый атрибут numberOfFloors = 10
В цикле пройдитесь по атрибуту numberOfFloors и распечайте значение "Текущий этаж равен"
Полученный код напишите в ответ к домашему заданию
Урок "Атрибуты и методы объекта"

"""


class House:
    def __init__(self, numberOfFloors, basement):
        self.numberOfFloors = numberOfFloors
        self.basement = basement


H15 = House(numberOfFloors = 15, basement = True)
H25 = House(numberOfFloors = 25, basement = True)
H3 = House(numberOfFloors = 3, basement = False)
print('Объект \"Дом в ', H15.numberOfFloors, 'этажей\" имеет id ', id(H15))
print('Объект \"Дом в ', H25.numberOfFloors, 'этажей\" имеет id ', id(H25))
print('Объект \"Дом в ', H3.numberOfFloors, 'этажей\" имеет id ', id(H3))

# Экземплярам класса House выше 9 этажей добавляем атрибут наличия лифта

for _ in [H3, H15, H25]:
    if _.numberOfFloors > 9:
        _.elevator = True
for _ in [H3, H15, H25]:
    if not _.basement:
        delattr(_, 'basement')

# Читаем атрибуты экземпляров и класса
for _ in [H3, H15, H25, House]:
    print(_.__dict__)
    for __ in range(_.numberOfFloors):
        print(__)


