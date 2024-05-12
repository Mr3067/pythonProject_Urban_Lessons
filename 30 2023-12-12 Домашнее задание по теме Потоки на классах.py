"""
2023/12/12 00:00|Домашнее задание по теме "Потоки на классах"

https://urban-university.ru/members/courses/course999421818026/20231212-0000domasnee-zadanie-po-teme-potoki-na-klassah-518653824735

"""
import threading
import random
import time


class Knight(threading.Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.enemy = 100
        self.days = 0
        self.lock = threading.RLock()
        self.lock2 = threading.Lock()

    def run(self):
        self.lock.acquire()
        print(f'{self.name},на нас напали!', flush=True)
        self.lock.release()
        while self.enemy > 0:
            time.sleep(random.random()/(random.random()+1))
            self.lock.acquire()
            print(21,self.lock2.acquire())
            print(22, self.lock2.release())
            self.enemy -= self.skill
            self.days += 1
            print(f'{self.name},сражается 1 день(дня)..., осталось {self.enemy} воинов.', flush=True)
            self.lock.release()
        print(f'{self.name},одержал победу спустя {self.days} дней!', flush=True)


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print(f'Все битвы закончились!')
