import multiprocessing
from time import sleep


def task_1():
    print("Multiprocessing number One - Start")
    a = 2
    b = 3
    result = a + b
    print(result)
    for i in range(1, 4):
        print(f"Инструкция {i} из процесса 1")
        sleep(1)
    print("Multiprocessing number One - Stop")


def task_2():
    print("Multiprocessing number Two - Start")
    text = "Text.... Someone else"
    print(text)
    for i in range(1, 4):
        print(f"Инструкция {i} из процесса 2")
        sleep(1)
    print("Multiprocessing number Two - Stop")


if __name__ == "__main__":
    print("Starting the main Process")

    t1 = multiprocessing.Process(target=task_1)
    t2 = multiprocessing.Process(target=task_2)
    # Тут запускаются дочерние потоки.
    t1.start()
    t2.start()
    # Пока дочерние потоки не закончат работу, не продолжат
    # выполняться инструкции из основного потока.
    t1.join()
    t2.join()

    print("Finishing the main Process")
