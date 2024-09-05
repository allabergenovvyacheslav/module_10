import queue
import random
from threading import Thread
from time import sleep


# #Класс Table:
# Объекты этого класса должны создаваться следующим способом - Table(1)
# Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)

# Класс Guest:
# Должен наследоваться от класса Thread (быть потоком).
# Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
# Обладать атрибутом name - имя гостя.
# Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.

# Класс Cafe:
# Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
# Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
# Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).


class Table:

    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(random.randint(3, 10))


class Cafe:

    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    # Метод guest_arrival(self, *guests):
    # Должен принимать неограниченное кол-во гостей (объектов класса Guest).
    # Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя и
    # выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
    # Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение
    # "<имя гостя> в очереди".

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    # Метод discuss_guests(self):
    # Этот метод имитирует процесс обслуживания гостей.
    # Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
    # Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive),
    # то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола>
    # свободен". Так же текущий стол освобождается (table.guest = None).
    # Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается
    # гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и
    # сел(-а) за стол номер <номер стола>"
    # Далее запустить поток этого гостя (start)

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} за столом {table.number} покушал(-а) и ушёл(ушла)')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен')
                if not self.queue.empty() and table.guest is None:
                    guest = self.queue.get()
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
    # Примечания:
    # Для проверки значения на None используйте оператор is (table.guest is None).
    # Для добавления в очередь используйте метод put, для взятия - get.
    # Для проверки пустоты очереди используйте метод empty.
    # Для проверки выполнения потока в текущий момент используйте метод is_alive.
    
    
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
