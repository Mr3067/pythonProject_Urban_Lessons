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
    def __init__(self, price=1000000, horse_powers=100):
        self.__price = price
        self.__horse_powers = horse_powers

    @property
    def horse_powers(self):
        return self.__horse_powers

    @horse_powers.setter
    def horse_powers(self, horse_powers):
        self.__horse_powers = horse_powers
        return self.__horse_powers

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
        return self.__price


class Nissan(Car):
    def __init__(self, price=2000002, horse_powers=125):
        super(Nissan,self).__init__(price, horse_powers)


class Kia(Car):
    def __init__(self, price=2500052, horse_powers=150):
        super(Kia, self).__init__(price, horse_powers)


c = Car()
print(c)
assert isinstance(c, Car)
assert c.price == 1000000
assert c.horse_powers == 100
assert c.__class__.__base__ == object

n = Nissan()
print(n)
assert isinstance(n, (Nissan, Car))
assert n.price == 2000002
assert n.horse_powers == 125
assert n.__class__.__base__ != object
assert n.__class__.__base__ == Car

k = Kia()
print(k)
assert isinstance(k, Kia)
assert k.price == 2500052
assert k.horse_powers == 150
assert k.__class__.__base__ != object
assert k.__class__.__base__ == Car
