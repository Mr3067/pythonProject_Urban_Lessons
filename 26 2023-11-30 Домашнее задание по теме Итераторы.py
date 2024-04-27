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
    def __init__(self, start=0.0, end=1.0):
        self.s = int(start)
        self.e = int(end)
        self.revers = 0

    def __iter__(self):
        if self.s > self.e:
            self.s, self.e = self.e, self.s
            self.revers = 1

        if self.e > 0:
            if self.s % 2 != 0:
                self.s += 1
            if self.e % 2 != 0:
                self.e -= 1

        elif self.e < 0:
            if self.s % 2 != 0:
                if self.s >= 0:
                    self.s -= 1
                else:
                    self.s += 1
            if self.e % 2 != 0:
                if self.e >= 0:
                    self.e += 1
                else:
                    self.e -= 1
        return self

    def __next__(self):
        if self.s > self.e:
            raise StopIteration
        if not self.revers:
            inner = self.s
            self.s += 2
            return inner
        else:
            inner = self.e
            self.e -= 2
            return inner


en = EvenNumbers(-9.1, 6.1)
for i in en:
    print(i)
