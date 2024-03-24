"""
https://urban-university.ru/members/courses/course999421818026/20231105-0000domasnee-zadanie-po-teme-nasledovanie-klassov-440919122156

ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/11/05 00:00|Домашнее задание по теме "Наследование классов"
Создайте новый проект или продолжите работу в текущем проекте

Ваша задача:
Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers, которая возвращает количество лошидиных сил для автомобиля
Создайте наследника класса Car - класс Nissan и переопределите свойство price, а также переопределите функцию horse_powers
Дополнительно создайте класс Kia, который также будет наследником класса Car и переопределите также свойство price, а также переопределите функцию horse_powers
Получившийся код прикрепите к заданию текстом

"""


class Car:
    price = 1000000

    def horse_powers(self):
        return 100


class Nissan(Car):
    price = 2000002

    def horse_powers(self):
        return 125


class Kia(Car):
    price = 2500052

    def horse_powers(self):
        return 150


c = Car()
print(c)
assert isinstance(c, Car)
assert c.price == 1000000
assert c.horse_powers() == 100
assert c.__class__.__base__ == object

n = Nissan()
print(n)
assert isinstance(n, (Nissan, Car))
assert n.price == 2000002
assert n.horse_powers() == 125
assert n.__class__.__base__ != object
assert n.__class__.__base__ == Car

k = Kia()
print(k)
assert isinstance(k, Kia)
assert k.price == 2500052
assert k.horse_powers() == 150
assert k.__class__.__base__ != object
assert k.__class__.__base__ == Car
