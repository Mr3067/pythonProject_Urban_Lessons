"""
ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/12/03 00:00|Домашнее задание по теме "Декораторы"
Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.

https://urban-university.ru/members/courses/course999421818026/20231203-0000domasnee-zadanie-po-teme-dekoratory-231730783138
"""

from functools import wraps


def gen_primes(n=2):
    """
    Генератор простых чисел в диапазоне от 2 до n
    :param n: верхний диапазон
    :return:
    """
    D = {}
    q = 2
    for i in range(n):
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def is_prime(func):
    """
    Функция декоратор
    """

    @wraps(func)
    def inner(*args):
        i = func(*args)
        return (f'Сумма = {i} Составное', f'Сумма = {i} Простое')[i in gen_primes(i + 1)]

    # inner.__name__ = func.__name__  # Замена декоратора wraps
    # inner.__doc__ = func.__doc__  # Замена декоратора wraps
    return inner


@is_prime
def sum_three(*args):
    """
    Функция принимает три положительных ненулевых значения и возвращает их сумму
    :param args: три значения для операции сложения
    :return: результат сложения трех значений
    """
    if len(args) != 3 or any(i <= 0 for i in args):
        raise ValueError
    return sum(args)


# sum_three = is_prime(sum_three)  # Декоратор через замыкание

print(sum_three(9900, 70, 3))
print(sum_three.__doc__)
