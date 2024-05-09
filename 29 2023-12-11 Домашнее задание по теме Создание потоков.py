"""
2023/12/11 00:00|Домашнее задание по теме "Создание потоков".
https://urban-university.ru/members/courses/course999421818026/20231211-0000domasnee-zadanie-po-teme-sozdanie-potokov-636521256211

"""
import time
import threading
import datetime

lock = threading.Lock()


def one_ten():
    for i in range(1, 10 + 1):
        lock.acquire()
        print(i, flush=True)
        lock.release()
        time.sleep(1)


def a_j():
    for i in range(ord('a'), ord('j') + 1):
        lock.acquire()
        print(chr(i), flush=True)
        lock.release()
        time.sleep(1)


start = datetime.datetime.now()
th1 = threading.Thread(target=one_ten)
th2 = threading.Thread(target=a_j)
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Время выполнения двух потоков: {datetime.datetime.now() - start}')
