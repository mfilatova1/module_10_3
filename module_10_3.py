from threading import Thread, Lock
from time import sleep
from random import randint, random

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            cash_in = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += cash_in
            print(f"Пополнение: {cash_in}. Баланс: {self.balance}")
            sleep(random())


    def take(self):
        for i in range(100):
            cash_out = randint(50, 500)
            print(f'Запрос на {cash_out}')
            if cash_out > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            else:
                self.balance -= cash_out
                print(f'Снятие {cash_out}:. Баланс: {self.balance}')
                sleep(random())



bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
