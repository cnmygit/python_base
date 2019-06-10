#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1+num2
        current += 1
        yield num
    return 'done'


if __name__ == "__main__":
    f = fib(5)
    while True:
        try:
            print(next(f))
        except StopIteration as e:
            print("⽣成器返回值:%s" % e.value)
            break

