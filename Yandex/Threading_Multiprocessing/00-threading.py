import threading
from time import sleep


def task_1():
    print("Threading number One - Start")
    a = 2
    b = 3
    result = a + b
    print(result)
    for i in range(1, 4):
        print(f'Инструкция {i} из потока 1')
        sleep(1)
    print("Threading number One - Stop")


def task_2():
    print("Threading number Two - Start")
    text = "Text.... Someone else"
    print(text)
    for i in range(1, 4):
        print(f'Инструкция {i} из потока 2')
        sleep(1)
    print("Threading number Two - Stop")


if __name__ == "__main__":
    print("Starting the main thread")

    t1 = threading.Thread(target=task_1)
    t2 = threading.Thread(target=task_2)
    # Тут запускаются дочерние потоки.
    t1.start()
    t2.start()
    # Пока дочерние потоки не закончат работу, не продолжат
    # выполняться инструкции из основного потока.
    t1.join()
    t2.join()

    print("inishing the main thread")
