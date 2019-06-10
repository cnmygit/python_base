#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time

g_num = 0

def work1(num):
    global g_num
    for i in range(num):
        g_num += 1

        # print("----in work1, g_num is %d---" % g_num)


def work2(num):
    global g_num
    for i in range(num):
        g_num += 1

        # print("----in work2, g_num is %d---" % g_num)


t1 = threading.Thread(target=work1, args=(1000000,))
t2 = threading.Thread(target=work2, args=(1000000,))
t1.start()
t2.start()

# 如果t1、t2未执行完，则休眠1s
while len(threading.enumerate()) != 1:
    time.sleep(1)

print("g_num最终值：%d" % g_num)