"""
https://urban-university.ru/members/courses/course999421818026/20231106-0000domasnee-zadanie-po-teme-mnozestvennoe-nasledovanie-290139472637

ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/11/06 00:00|Домашнее задание по теме "Множественное наследование"
Создайте новый проект или продолжите работу в текущем проекте

Ваша задача:
Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers, которая возвращает количество лошидиных сил для автомобиля
Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type, а также переопределите функцию horse_powers
Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price
"""


class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self):
        return 150


class Nissan(Vehicle, Car):
    def __init__(self):
        self.price = super().price * 1.2
        self.vehicle_type = super().vehicle_type + self.__class__.__name__


v = Vehicle()
c = Car()
n = Nissan()
print(v.__dict__.items(), v.vehicle_type)
print(c.__dict__.items(), c.price, c.horse_powers())
print(n.__dict__.items())