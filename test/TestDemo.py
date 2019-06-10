#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Iterable


class FibIterator(object):
    """斐波那契数列迭代器"""
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.num1 = 0
        self.num2 = 1

    def __next__(self):
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1+self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__返回⾃⾝即可"""
        return self


if __name__ == "__main__":

    fibiterator = FibIterator(10)

    # for i in fibiterator:
    #     print(i, end="、")

    # print(list(fibiterator))

    print(tuple(fibiterator))