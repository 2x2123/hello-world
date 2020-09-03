from multiprocessing import Process, Semaphore, Lock, Queue
from random import random
import time


buffer = Queue(10)
empty = Semaphore(2)
full = Semaphore(0)
lock = Lock()


class Consumer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            full.acquire()
            lock.acquire()
            print(f'Consumer get {buffer.get()}')
            time.sleep(1)
            lock.release()
            empty.release()


class Producer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            empty.acquire()
            lock.acquire()
            num = random()
            print(f'Producer put {num}')
            buffer.put(num)
            time.sleep(1)
            lock.release()
            full.release()


if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Main Process Ended')
