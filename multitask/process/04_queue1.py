#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Queue, Process
import time, random


def write(q):
    if not q.full():
        for value in ["a", "b", "c", "d"]:
            print("向队列中添加消息 %s" % value)
            q.put(value)
            time.sleep(random.random())


def read(q):
    while True:
        if not q.empty():
            for i in range(q.qsize()):
                print(q.get())
                time.sleep(random.random())
        else:
            break


if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=write, args=(q,))
    p1.start()
    p1.join()

    p2 = Process(target=read, args=(q,))
    p2.start()
    p2.join()