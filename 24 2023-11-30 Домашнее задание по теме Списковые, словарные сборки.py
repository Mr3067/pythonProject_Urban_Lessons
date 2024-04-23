"""
ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/11/30 00:00|Домашнее задание по теме "Списковые, словарные сборки"
Цель работы
Освоить механизмы работы встроенных функций map и filter. Закрепить их различия и узнать, как передавать пользовательскую функцию, как аргумент в функции map и filter.
Задание
Дан список целых чисел, примените функции map и filter так, чтобы в конечном списке оставить нечётные квадраты чисел
Примечание
Не забывайте, что встроенные функции map и filter возвращают генератор, сами операции преобразования не выполняются.


"""

innlist = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

print(list(filter(lambda x: x % 2 != 0, map(lambda x: x ** 2, innlist))))
