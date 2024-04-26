"""
ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/11/30 00:00|Домашнее задание по теме "Итераторы"
Цель работы
Применить dunder методы iter, next в своём классе
Задание
Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне. При создании и инициализации объекта этого класса создаются атрибуты:
start – начальное значение (если значение не передано, то 0)
end – конечное значение (если значение не передано, то 1)

"""


class EvenNumbers:
    def __init__(self, start=0, end=1):
        if abs(start) > abs(end):
            raise TypeError
        self.s = int(start)
        self.e = int(end)
        # print(self.s, self.e)
        if self.e < 0:
            if self.s > start:
                self.s -= 1
            if self.s % 2 != 0:
                self.s -= 1
        if self.e > 0:
            if self.s % 2 != 0:
                self.s += 1
        # print(self.s,self.e)
    def __iter__(self):
        return self

    def __next__(self):
        if self.e > 0:
            if self.s > self.e:
                raise StopIteration
            innindex = self.s
            self.s += 2
            return innindex
        if self.e < 0:
            if self.s < self.e:
                raise StopIteration
            innindex = self.s
            self.s -= 2
            return innindex


en = EvenNumbers(10, -25)

for i in en:
    print(i)
