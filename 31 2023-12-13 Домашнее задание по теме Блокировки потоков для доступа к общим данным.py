"""
2023/12/13 00:00|Домашнее задание по теме "Блокировки потоков для доступа к общим данным"
https://urban-university.ru/members/courses/course999421818026/20231213-0000domasnee-zadanie-po-teme-blokirovki-potokov-dla-dostupa-k-obsim-dannym-793684761441
"""
import threading


class BankAccount:
    def __init__(self, balance=1000, amount=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lock = threading.Lock()
        self.balance = balance
        self.amount = amount

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f'Deposited {amount}, new balance is {self.balance}')

    def withdraw(self, amount):
        with self.lock:
            self.balance -= amount
            print(f'Withdrew {amount}, new balance is {self.balance}')


def deposit_task(account, amount):
    if isinstance(account, BankAccount):
        for _ in range(5):
            account.deposit(amount)


def withdraw_task(account, amount):
    if isinstance(account, BankAccount):
        for _ in range(5):
            account.withdraw(amount)


account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
