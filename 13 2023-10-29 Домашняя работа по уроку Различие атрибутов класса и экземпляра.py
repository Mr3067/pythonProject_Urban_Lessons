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
    counterFloorTotle = 0

    def __init__(self, name=None, number_of_floor=0):
        self.name = name
        self.numberOfFloor = number_of_floor
        Building.counterBilding += 1
        print(f'Сообщение Building.__init__ Создан объект {self.name} экземпляр №{Building.counterBilding} '
              f'класса {self.__class__}')

    def __del__(self):
        Building.counterBilding -= 1
        print(f'Удален объект {self.name}. Всего экземпляров класса {self.__class__} '
              f'осталось {Building.counterBilding}')



arrayBuildings = []  # список для экземпляров класса
LenOfArr = int(input(f'Введите размер создаваемого списка экземпляров класса {Building.__name__} (целое число):'))

for _ in range(1, LenOfArr + 1):  # заполнение списка экземплярами класса
    arrayBuildings.append(Building(name=f'Building №{_}', number_of_floor=0))

print(f'\nВсего создано {Building.counterBilding} экземпляров согласно счетчика класса\n')
input('\nНажмите Enter для продолжения\n')

print(f'\nВывод имен экземпляров класса:\n')
for i in range(0, LenOfArr):  # вывод заполненного списка
    print(arrayBuildings[i].name)

input('\nНажмите Enter для продолжения\n')

random.shuffle(arrayBuildings)  # персортица элементов списка
for i in range(0, LenOfArr):
    arrayBuildings[i].numberOfFloor = random.choice([i for i in range(1,10)])
    print(arrayBuildings[i].numberOfFloor)

print(f'\nВывод имен экземпляров класса после пересортицы:\n')
for i in range(0, LenOfArr):  # измененный список
    Building.counterFloorTotle += arrayBuildings[i].numberOfFloor
    print(f'Здание:{arrayBuildings[i].name},\t количество этажей здания: {arrayBuildings[i].numberOfFloor}')

print(f'\nОбщее количество этажей всех зданий: {Building.counterFloorTotle}\n')

input('\nНажмите Enter для удаление объектов класса Building\n')
# наблюдаем в какой последовательности удаляются экземпляры класса. Порядок удаления не равен порядку инициализации
