"""
2023/11/25 00:00|Домашнее задание по теме "Работа с классом Warning"
Цель задания:

Освоить механизмы создания и обработки исключений в Python.
Научиться создавать собственные исключения, наследуя классы от Exception. Попрактиковаться в передаче исключений дальше по стеку вызовов.

Задание:

Импортируйте модуль warnings.
Реализуйте функцию для расчёта деления, которая будет генерировать предупреждение, если делитель близок к нулю (например, меньше 0.01), предупреждая об опасности деления на ноль.
Сгенерируйте UserWarning в этом случае.
Используйте разные фильтры для управления поведением программы при появлении такого предупреждения: always, ignore, error

"""
import warnings


# фильтры класса "error", "ignore", "always", "default", "module","once"

def my_div_error(a=5, b=0.009):
    warnings.simplefilter("error")
    if b < 0.01:
        try:
            warnings.warn("Сообщение генерирует ошибку №1", UserWarning)
            warnings.warn("Сообщение генерирует ошибку №1", UserWarning)
        except UserWarning:
            print('Сгенерирована ошибка')
    return a / b


def my_div_ignore(a=5, b=0.009):
    warnings.simplefilter("ignore")
    if b < 0.01:
        warnings.warn("Сообщение генерирует ошибку №1", UserWarning)
        warnings.warn("Сообщение генерирует ошибку №1", UserWarning)
    return a / b


def my_div_always(a=5, b=0.009):
    warnings.simplefilter("always")
    if b < 0.01:
        warnings.warn("Сообщение генерирует ошибку №1", UserWarning)
        warnings.warn("Сообщение генерирует ошибку №1", UserWarning)
    return a / b


def my_div_default(a=5, b=0.009):
    warnings.simplefilter("default")
    if b < 0.01:
        warnings.warn("Сообщение генерирует ошибку №1", UserWarning)
        warnings.warn("Сообщение генерирует ошибку №1", UserWarning)
    return a / b


def my_div_module(a=5, b=0.009):
    warnings.simplefilter("module")
    if b < 0.01:
        warnings.warn("Сообщение генерирует ошибку №1", UserWarning)
        warnings.warn("Сообщение генерирует ошибку №1", UserWarning)
    return a / b


def my_div_once(a=5, b=0.009):
    warnings.simplefilter("once")
    if b < 0.01:
        warnings.warn("Сообщение генерирует ошибку №1", UserWarning)
        warnings.warn("Сообщение генерирует ошибку №1", UserWarning)
    return a / b

