"""
Демонстрация понятия множества потоков в одном и том же процессе.
"""
from abc import abstractmethod
from threading import Thread
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
        thread_count_down(self.name, self.delay)
        print('\t\tFinished thread %s' % self.name)


def thread_count_down(name, delay):
    """Фукнкция задержки времени."""
    counter = 5

    while counter:
        sleep(delay)
        print('\t\t\tThread %s counting down: %i...' % (name, counter))
        counter -= 1

if __name__ == '__main__':
    
    thread1 = MyThread('thread1', 0.5)
    thread2 = MyThread('thread2', 0.75)

    print('PROGRAMM')

    print('\trun...')
    thread1.run()
    thread2.run()

    print('\tstart...')
    thread1.start()
    thread2.start()

    print('\tjoin...')
    thread1.join()
    thread2.join()
    
    print('FINISHED')

# 15:29:15 > python -i 100_flows.py
# PROGRAMM
#     run...
#         Starting thread thread1
#             Thread thread1 counting down: 5...
#             Thread thread1 counting down: 4...
#             Thread thread1 counting down: 3...
#             Thread thread1 counting down: 2...
#             Thread thread1 counting down: 1...
#         Finished thread thread1
#             Starting thread thread2
#             Thread thread2 counting down: 5...
#             Thread thread2 counting down: 4...
#             Thread thread2 counting down: 3...
#             Thread thread2 counting down: 2...
#             Thread thread2 counting down: 1...
#         Finished thread thread2
#     start...
#         Starting thread thread1
#         Starting thread thread2
#     join...
#             Thread thread1 counting down: 5...
#             Thread thread2 counting down: 5...
#             Thread thread1 counting down: 4...
#             Thread thread1 counting down: 3...
#             Thread thread2 counting down: 4...
#             Thread thread1 counting down: 2...
#             Thread thread2 counting down: 3...
#             Thread thread1 counting down: 1...
#         Finished thread thread1
#             Thread thread2 counting down: 2...
#             Thread thread2 counting down: 1...
#         Finished thread thread2
# FINISHED