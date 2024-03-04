"""
https://urban-university.ru/members/courses/course999421818026/20231027-0000domasnaa-rabota-po-uroku-specialnye-metody-klassov-854615870903

ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/10/27 00:00|Домашняя работа по уроку "Специальные методы классов"
Домашнее задание по уроку "Пространство имен"

Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новый класс House
Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на параметр floors и
выводить в консоль numberOfFloors
Полученный код напишите в ответ к домашему заданию


"""

class House:

    def decoratorNunberFloor(func):
        if func.__name__ == '__init__':
            outstr = 'init has been run'
        elif func.__name__ == 'setNewNumberOfFloors':
            outstr = 'set has been change NewNumberOfFloors attribute'

        def inner(*args, **kwargs):
            if len(args) == 1:
                print('\nNumber of floors couldn\'t be None\n\nNewNumberOfFloors = 0 when '+outstr)
                func(*args, **kwargs)
            else:

                if args[1] < 0:
                    print('\nNumber of floors couldn\'t be below zero\n\nNewNumberOfFloors = 0 when '+outstr)
                    func(*args, **kwargs)

                elif args[1] == 0 :
                    print(f'Number of floors is {args[1]} when '+outstr)
                    func(*args, **kwargs)
                elif args[1] == 1:
                    print(f'Number of floors is {args[1]} when '+outstr)
                    func(*args, **kwargs)
                else:
                    print(f'Number of floors are {args[1]} when '+outstr)
                    func(*args, **kwargs)
        return inner


    @decoratorNunberFloor
    def __init__(self,  numberOfFloors = 0):
        self.NewNumberOfFloors = numberOfFloors


    @decoratorNunberFloor
    def setNewNumberOfFloors(self, floors=0):
        self.NewNumberOfFloors = floors

