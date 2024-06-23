import unittest
from HW_38 import Student


class Student_test(unittest.TestCase):

    def setUp(self):
        self.vasily = Student('Vasiliy')
        self.vasily.distance = 0
        self.gennadiy = Student('Gennadiy')
        self.gennadiy.distance = 0

    """
    Первый тест: у одного объекта должен запускать метод walk 10 раз, 
    после чего должен возвращаться результат сравнения полученных данных. 
    В случае провального теста должно выводится сообщение: 
    Дистанции не равны [дистанция человека(объекта)] != 500
    """

    def test_walk_10_times(self):
        for times in range(10):
            self.vasily.walk()

        self.assertEqual(self.vasily.distance,
                         500,
                         f'Дистанции не равны {self.vasily.distance}] != 500')

    """
    Второй тест: 
    у одного объекта должен запускать метод run 10 раз, 
    после чего должен возвращаться результат сравнения полученных данных. 
    В  случае провального теста должно выводится сообщение: 
    Дистанции не равны [дистанция человека(объекта)] != 1000
    
    """

    def test_run_10_times(self):
        for times in range(10):
            self.vasily.run()

        self.assertEqual(self.vasily.distance,
                         1000,
                         f'Дистанции не равны {self.vasily.distance}] != 1000')

    """
    Третий тест: 
    2 объекта "соревнуются", один "бежит", другой "идёт" (тот самый студент, кто не посещает вебинары). 
    После чего должен возвращаться результат сравнения полученных данных. 
    В  случае провального теста должно выводится сообщение: 
    бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек].
    """

    def test_comp(self):
        self.vasily.run()
        self.gennadiy.walk()
        self.assertGreater(self.vasily.distance,
                           self.gennadiy.distance,
                           f'{self.vasily.name} должен преодолеть дистанцию больше, чем {self.gennadiy.name}')


if __name__ == '__main__':
    unittest.main()
