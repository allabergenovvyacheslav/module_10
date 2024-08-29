# Задача "Потоковая запись в файлы":

# Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество
# записываемых слов, file_name - название файла, куда будут записываться слова.

# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий
# файл с прерыванием после записи каждого на 0.1 секунду.

# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её:
# from time import sleep.

# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
#
# После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:

# 10, example1.txt
# 30, example2.txt
# 200, example3.txt
# 100, example4.txt

# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:

# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt

# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в
# лекции к домашнему заданию.

import threading, time, datetime

time_start = datetime.datetime.now()


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i + 1}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.datetime.now()
time_res = time_end - time_start
print(time_res)

time_start = datetime.datetime.now()

thr = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thr1 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thr2 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thr3 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thr.start()
thr1.start()
thr2.start()
thr3.start()

thr.join()
thr1.join()
thr2.join()
thr3.join()

time_end = datetime.datetime.now()
time_res = time_end - time_start
print(time_res)
