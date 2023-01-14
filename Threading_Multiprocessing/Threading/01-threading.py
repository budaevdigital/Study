from threading import Lock, Thread

counter = 0


# Объект блокировки, нужен для синхронизации потоков
# перед изменением счётчика
lock = Lock()


def increment_value():
    global counter
    for count in range(10**6):
        # Синхронизируем потоки в контекстном менеджере
        with lock:
            counter += 1


new_thread_first = Thread(target=increment_value)
new_thread_first.start()

new_thread_second = Thread(target=increment_value)
new_thread_second.start()

new_thread_first.join()
print(counter)

new_thread_second.join()
print(counter)

print(10**6)
