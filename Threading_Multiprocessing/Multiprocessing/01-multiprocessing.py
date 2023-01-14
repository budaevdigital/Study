import os
import time
from multiprocessing import Process


def just_printer(name: str):
    time.sleep(500)
    print("hello", name)


if __name__ == "__main__":
    try:
        new_process = Process(target=just_printer, args=("David",))
        new_process.start()
        print("Process is start")
        # Выведем ID текущего процесса
        print("Parent PID ", os.getpid())
        # и ID процесса, который был запущен
        print("Child PID ", new_process.pid)
        new_process.join()
    except KeyboardInterrupt as er:
        pass
    finally:
        print("Done!")

# Созданные процессы можно посмотреть ps aux | grep <pid_number>
