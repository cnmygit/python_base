#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import time
import os

# 进程间不共享全局变量！！！！！！！！！！！！！
list1 = [1,2]

def work1():
    """⼦进程要执⾏的代码"""
    print('in process1，pid=%d, list=%s' % (os.getpid(), list1))
    for i in range(3):
        list1.append(i)
        time.sleep(0.2)
        print('in process1，pid=%d, list=%s' % (os.getpid(), list1))


def work2():
    print('in process2，pid=%d, list=%s' % (os.getpid(), list1))


if __name__ == "__main__":
    print('⽗进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号
    p1 = Process(target=work1)
    p1.start()
    # Join()是主程序等我这个进程执行完毕了，程序才往下走
    p1.join()

    p2 = Process(target=work2)
    p2.start()