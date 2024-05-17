"""
ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/12/19 00:00|Домашнее задание по теме "Многопроцессное программирование"

https://urban-university.ru/members/courses/course999421818026/20231219-0000domasnee-zadanie-po-teme-mnogoprocessnoe-programmirovanie-206781820586

"""

from multiprocessing import Process, Queue
from os import getpid, getppid, cpu_count
from collections import defaultdict


class WarehouseManager:
    product_queue = Queue()

    def __init__(self):
        self.data = defaultdict(int)
        print(self.data)

    def process_request(self, request: tuple, product_queue):
        if request[1] == "receipt":
            a = (request[0], request[2])
            product_queue.put(a)
        elif request[1] == "shipment":
            a = (request[0], request[2] * (-1))
            product_queue.put(a)

    def run(self, requests):
        process_list = []
        for _ in requests:
            process_list.append(Process(target=self.process_request, args=(_, WarehouseManager.product_queue)))
            process_list[-1].start()
        for _ in process_list:
            _.join()
        for i in range(WarehouseManager.product_queue.qsize()):
            inner = WarehouseManager.product_queue.get()
            if inner[1] < 0 and abs(self.data[inner[0]]) < abs(inner[1]):
                print(f'Недостаточно товара. Товара {inner[0]} в количестве {inner[1]} нет.'
                      f'Будет отгружено {self.data[inner[0]]}')
                self.data[inner[0]] -= self.data[inner[0]]
            else:
                self.data[inner[0]] += inner[1]
        self.data = dict(self.data)


if __name__ == '__main__':
    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    # requests = [
    #     ("product1", "receipt", 100),
    #     ("product2", "shipment", 150),
    #     ("product3", "receipt", 130),
    #     ("product1", "shipment", 200),
    #     ("product2", "receipt", 50),
    #     ("product3", "shipment", 130),
    #     ("product1", "receipt", 200),
    #     ("product2", "shipment", 50),
    #     ("product3", "receipt", 130),
    #     ("product1", "shipment", 200),
    #     ("product2", "receipt", 50)
    # ]

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)
    #
    # # Выводим обновленные данные о складских запасах
    print(manager.data)
