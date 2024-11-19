from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(word_count):
            print("Какое-то слово №", i + 1, file=f)
            sleep(0.1)
        print("Завершилась запись в файл", file_name)

# Вызов функции 4 раза с разными аргументами
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

# Создание потоков для вызова функции с другими аргументами
from threading import Thread

threads = [
    Thread(target=write_words, args=(10, "example5.txt")),
    Thread(target=write_words, args=(30, "example6.txt")),
    Thread(target=write_words, args=(200, "example7.txt")),
    Thread(target=write_words, args=(100, "example8.txt"))
]

# Запуск потоков и ожидание их завершения
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()