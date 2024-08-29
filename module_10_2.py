import threading
import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        day_war = 10
        soldier = 100
        print(f'{self.name}, на нас напали!')
        time.sleep(1)
        for j in range(day_war):
            time.sleep(1)
            print(f'{self.name} сражается {j + 1} день(дня)..., осталось {soldier - self.power} воинов')
        time.sleep(1)
        print(f'{self.name} одержал победу спустя {day_war} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
first_knight.join()
second_knight.start()
second_knight.join()


print(f'Все битвы закончились!')

