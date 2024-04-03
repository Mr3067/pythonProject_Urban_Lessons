"""
ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/11/16 00:00|Домашнее задание по теме "Файлы в операционной системе".
Цель задания:

Освоить работу с файловой системой в Python, используя модуль os.
Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize и использование модуля time для корректного отображения времени.

Задание:

Создайте новый проект или продолжите работу в текущем проекте.
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.

"""
import os,time

for (dirpath, dirnames, filenames) in os.walk('.'):

    for dirname in dirnames:
        for filename in filenames:
            print(f'Обнаружен файл: {filename}, Путь: {os.path.join(dirpath, filename)}, Размер: {os.path.getsize(filename)} байт, Время изменения: {time.ctime(os.path.getmtime(filename))}, Родительская директория: {os.path.split(os.getcwd())[0]}')




