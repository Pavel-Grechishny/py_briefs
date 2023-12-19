from threading import Thread, Lock
from time import sleep


class MyThread(Thread):
    """Описывает поток."""

    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        """Выполняет произвольную операцию."""
        print('\t\tStarting thread %s' % self.name)
        thread_lock.acquire() # Объект блокировки потока начало
        thread_count_down(self.name, self.delay)
        thread_lock.release() # Объект блокировки потока завершение
        print('\t\tFinished thread %s' % self.name)


def thread_count_down(name, delay):
    """Фукнкция задержки времени."""
    counter = 5

    while counter:
        sleep(delay)
        print('\t\t\tThread %s counting down: %i...' % (name, counter))
        counter -= 1


if __name__ == '__main__':
    # Объект блокировки потока создание экземпляра
    thread_lock = Lock()

    thread1 = MyThread('A', 0.5)
    thread2 = MyThread('B', 0.3)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

# 17:19:11 > python -i html\test.py
# Starting thread A
# Starting thread B
#         Thread A counting down: 5...
#         Thread A counting down: 4...
#         Thread A counting down: 3...
#         Thread A counting down: 2...
#         Thread A counting down: 1...
# Finished thread A
#         Thread B counting down: 5...
#         Thread B counting down: 4...
#         Thread B counting down: 3...
#         Thread B counting down: 2...
#         Thread B counting down: 1...
# Finished thread B
# >>>
