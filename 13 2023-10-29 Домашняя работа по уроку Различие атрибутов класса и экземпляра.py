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


class Building:
    counterBilding = 0

    def __init__(self, name=None, numberOfFloor=0):
        self.name = name
        self.numberOfFloor = numberOfFloor
        Building.counterBilding += 1
        print(f'Создан объект {self.name} экземпляр №{Building.counterBilding} класса {self.__class__}')

    def __del__(self):
        Building.counterBilding -= 1
        print(f'Удален объект {self.name}. Всего экземпляров класса {self.__class__} осталось {Building.counterBilding}')


arrayBuildings = []

for _ in range(1,  5):
    arrayBuildings.append(Building(name=f'Building №{_}', numberOfFloor=0))
    print(arrayBuildings[_-1])
for i in range(4):
    print(arrayBuildings[i].name)
arrayBuildings.append(arrayBuildings.pop(1))
for i in range(4):
    print(arrayBuildings[i].name)

input('Нажмите Enter для удаление объектов класса Building')
