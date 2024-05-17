"""
ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/12/16 00:00|Домашнее задание по теме "Очереди для обмена данными между потоками."
"""

from threading import Thread, Lock, get_ident
from time import sleep
from os import getpid
from queue import Queue
from random import random

table_queue = Queue()  # Очередь столов
customer_queue = Queue()  # Очередь клиентов


class Table:
    def __init__(self, number, is_busy=True):  # is_busy = True - стол свободен
        self.number = number
        self.is_busy = is_busy
        table_queue.put((self.number, self.is_busy))  # Заполняет очередь столов


class Customer(Thread):  # В очередь добавляются клиенты при условии длины очереди меньше 5.
    customer_number = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            if not table_queue.empty() and customer_queue.empty() or table_queue.qsize() > customer_queue.qsize():
                Customer.customer_number += 1
                print(f'Посетитель номер {Customer.customer_number} прибыл.')
                customer_queue.put(Customer.customer_number)
                sleep(1)
            elif table_queue.empty() and customer_queue.qsize() < 5:
                Customer.customer_number += 1
                print(f'Посетитель номер {Customer.customer_number} прибыл.')
                print(f'Посетитель номер {Customer.customer_number} ожидает свободный стол.')
                customer_queue.put(Customer.customer_number)
                sleep(1)
            elif table_queue.empty() and customer_queue.qsize() >= 5:
                print(f'Перед вами очередь {customer_queue.qsize()} '
                      f'человек.Столов мало, очередь не занимать! Идите в "Вкусно и точка"')
                while table_queue.empty():  # ожидание свободного стола
                    sleep(0.01)


class Cafe:
    def __init__(self, tables):
        self.lock = Lock()
        self.tables = tables

    def customer_take_table(self, customer, table):
        self.lock.acquire()
        inn_table = table.get()[0]
        inn_customer = customer.get()
        print(f'Посетитель номер {inn_customer} сел за стол {inn_table}.')
        self.lock.release()
        sleep(7)
        print(f'Посетитель номер {inn_customer} покушал и ушёл. Стол {inn_table} освободился.')
        table.put((inn_table, True))

    def serve_customer(self, customer, table):
        while True:
            for _ in range(table_queue.qsize()):
                if not customer.empty():
                    Thread(target=self.customer_take_table, args=(customer, table)).start()

    def customer_arrival(self):
        Customer().start()
        inn_serve = Thread(target=self.serve_customer, args=(customer_queue, table_queue))
        inn_serve.start()
        inn_serve.join()


if __name__ == '__main__':
    # Создаем столики в кафе
    table1 = Table(1)
    table2 = Table(2)
    table3 = Table(3)
    # table4 = Table(4)
    # table5 = Table(5)
    # table6 = Table(6)
    # table7 = Table(7)
    # table8 = Table(8)
    # table9 = Table(9)
    # table10 = Table(10)
    tables = []
    # Инициализируем кафе
    cafe = Cafe(tables)

    # Запускаем поток для прибытия посетителей
    customer_arrival_thread = Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()

    # Ожидаем завершения работы прибытия посетителей
    customer_arrival_thread.join()
