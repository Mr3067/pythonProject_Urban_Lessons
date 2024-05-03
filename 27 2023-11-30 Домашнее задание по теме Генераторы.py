"""
ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/11/30 00:00|Домашнее задание по теме "Генераторы"
Цель работы
Более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.
Задание
Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки. В функцию передаётся только сама строка.

"""
def all_variants(in_str):
    n = len(in_str)
    for k in range(n+1):
        inn_list = [i for i in range(k)] + [n] + [0]
        while True:
            yield ''.join([in_str[iii] for iii in inn_list[:k]])
            for i in range(len(inn_list) - 1):
                if inn_list[i] + 1 == inn_list[i + 1]:
                    inn_list[i] = i
                else:
                    break
            if i < k:
                inn_list[i] += 1
            else:
                break


a = all_variants("abc125")
for i in a:
    print(i)

