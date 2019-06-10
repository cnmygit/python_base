#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


class MyThread(threading.Thread):

    def run(self):
        for i in range(5):
            time.sleep(0.5)
            msg = "I'm "+self.name+' @ '+str(i) #name属性中保存的是当前线程的名字
            print(msg)


def test():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == "__main__":
    test()