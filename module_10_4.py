import queue
from threading import Thread
from time import sleep
import random


# def producer(queue):
#     while True:
#         message = 'ping'
#         queue.put(message)
#         sleep(random.randint(2, 6))
#
#
# def worker(queue):
#     while True:
#         message = queue.get()
#         print(message)
#
#
# q = queue.Queue()
# t1 = Thread(target=producer, args=(q,))
# t2 = Thread(target=worker, args=(q,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

class Table:

    def __init__(self, *number):
        self.number = number
        self.guest = None


class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(random.randint(3, 10))


class Cafe:

    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for table in self.tables:
            for guest in guests:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                else:
                    self.queue.put(guest.name)
                    print(f'{guest.name} в очереди')

# Метод discuss_guests(self):
# Этот метод имитирует процесс обслуживания гостей.
#
# Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
#
# Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive),
# то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола>
# свободен". Так же текущий стол освобождается (table.guest = None).
#
# Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу
# присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди>
# вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
#
# Далее запустить поток этого гостя (start)

    def discuss_guests(self):
        # Функция any() в Python, хотя бы один элемент True
        while any(table.guest is not None for table in self.tables or not self.queue.empty()):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest.join()
                        if not self.queue.empty() and table.guest is None:
                            table.guest = self.queue.get()
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) '
                                  f'за стол номер {table.number}')
                            table.guest.start()

if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()








