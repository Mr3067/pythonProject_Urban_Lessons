"""
https://urban-university.ru/members/courses/course999421818026/20231029-0000domasnaa-rabota-po-uroku-razlicie-atributov-klassa-i-ekzemplara-898418567750

ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/10/29 00:00|Домашняя работа по уроку "Различие атрибутов класса и экземпляра."
Домашнее задание по уроку "Различие атрибутов класса и экземпляра"

Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новый класс Buiding с атрибутом total
Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов класса Building total (по примеру класса Lemming из урока)
В цикле создайте 40 объектов класса Building и выведите их на экран командой print
Полученный код напишите в ответ к домашему заданию
Урок "Различие атрибутов класса и экземпляра"

"""

import random


class Building:
    counterBilding = 0

    def __init__(self, name=None, numberOfFloor=0):
        self.name = name
        self.numberOfFloor = numberOfFloor
        Building.counterBilding += 1
        print(f'Сообщение Building.__init__ Создан объект {self.name} экземпляр №{Building.counterBilding} класса {self.__class__}')

    def __del__(self):
        Building.counterBilding -= 1
        print(f'Удален объект {self.name}. Всего экземпляров класса {self.__class__} осталось {Building.counterBilding}')


arrayBuildings = [] # список для экземпляров класса
randomLenOfArr = random.randint(5, 10)  # выбор случайного размера списка объектов в заданном диапазоне

for _ in range(1, randomLenOfArr): # заполнение списка экземплярами класса
    arrayBuildings.append(Building(name=f'Building №{_}', numberOfFloor=0))
print(f'\nВсего создано {Building.counterBilding} экземпляров согласно счетчика класса\n')
input('\nНажмите Enter для продолжения\n')
print(f'\nВывод имен экземпляров класса:\n')
for i in range(randomLenOfArr - 1): # вывод заполненного списка
    print(arrayBuildings[i].name)

input('\nНажмите Enter для продолжения\n')

for i in range(randomLenOfArr - 1): # бестолковая работа с элементами списка, создание пересортицы
    arrayBuildings.append(arrayBuildings.pop(randomLenOfArr - 2 - int(random.randint(0, randomLenOfArr - 2))))

print(f'\nВывод имен экземпляров класса после пересортицы:\n')
for i in range(randomLenOfArr - 1): # измененный список
    print(arrayBuildings[i].name)

input('\nНажмите Enter для удаление объектов класса Building\n')
# наблюдаем в какой последовательности удаляются экземпляры класса. Порядок удаления не равен порядку инициализации
