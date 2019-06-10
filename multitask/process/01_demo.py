#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import time
import os


def run_proc(name, age,  **kwargs):
    """⼦进程要执⾏的代码"""
    for i in range(10):
        print('⼦进程运⾏中， name= %s,age=%d ,pid=%d...' % (name, age, os.getpid()))
        print(kwargs)
        time.sleep(0.2)
    print('⼦进程将要结束...')


if __name__ == "__main__":
    print('⽗进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号
    p = Process(target=run_proc, args=("test", 18), kwargs={"m":20})
    p.start()
    time.sleep(1)
    p.terminate()
