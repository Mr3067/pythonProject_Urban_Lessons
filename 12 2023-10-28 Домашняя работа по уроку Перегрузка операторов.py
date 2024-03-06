"""
https://urban-university.ru/members/courses/course999421818026/20231028-0000domasnaa-rabota-po-uroku-peregruzka-operatorov-383353110577

ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/10/28 00:00|Домашняя работа по уроку "Перегрузка операторов."
Домашнее задание по уроку "Перегрузка операторов"

Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новый класс Buiding
Создайте инициализатор для класса Buiding, который будет задавать целочисленный атрибут этажности self.numberOfFloors и
строковый атрибут self.buildingType
Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
Полученный код напишите в ответ к домашему заданию
Урок "Перегрузка операторов"

"""


class Building:
    def inputDecorator(func):
        def inner(self, *args, **kwargs):
            if len(args) != 2:
                inputnumberOfFloors = int(input('Введите количество этажей объекта (целое число):'))
                inputbuildingType = input('Введите тип объекта (дом, таунхауз, сарай, гараж):')
                func(self, inputnumberOfFloors, inputbuildingType)
            else:
                func(self, *args, **kwargs)

        return inner

    @inputDecorator
    def __init__(self, numberOfFloors, buildingType):
        if isinstance(numberOfFloors, (int)):
            self.numberOfFloors = numberOfFloors
        else:
            exit()
        if buildingType in [' ', 'дом', 'таунхауз', 'сарай', 'гараж']:
            self.buildingType = buildingType
        else:
            exit()

    def __eq__(self, other):
        if isinstance(other, Building):
            if self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType:
                print('\nObjects are equal\n')
                return True
            else:
                print('\nObjects are not equal\n')
                return False
        else:
            print(f'Object {other} is {other.__class__}. Not {self.__class__}')
