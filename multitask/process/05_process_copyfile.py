#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing
import os
import time
import random


# 01.py test test-备份 队列
def copy_file(file_name, src, dest, queue):
    """拷⻉⽂件的函数"""
    # test/01.py ----》 test-备份/01.py
    # 打开⽂件资源
    src_file = open(src + '/' + file_name, "rb")
    dest_file = open(dest + '/' + file_name, "wb")
    # 读取源⽂件 写⼊到⽬标⽂件中
    while True:
        data = src_file.read(4096)
        if data:
            dest_file.write(data)
        else:
            break

    time.sleep(random.random())
    # 关闭⽂件资源
    src_file.close()
    dest_file.close()
    queue.put(file_name)



if __name__ == '__main__':
    # 获取⽤⼾的源⽬录 test
    src_path = "D:/develop/python_workspace/temp/a"
    try:
        # 创建⼀个和源目录很像的目录 test-备份
        dest_path = src_path + "-备份"
        os.mkdir(dest_path)
        # 获取源⽬录下的所有⽂件列表
        file_list = os.listdir(src_path)
        # print(file_list)
    except Exception as e:
        print(e)
    else:
        queue = multiprocessing.Queue()
        # 为每个⽂件创建⼀个进程进⾏拷⻉
        for file in file_list:
            pro = multiprocessing.Process(target=copy_file, args=(file, src_path, dest_path, queue))
            pro.start()

        # 每拷⻉完⼀个⽂件 显⽰进度 已完成的⽂件数量/总量
        # 通过参数将⼀个队列传⼊到进程中
        # 已经拷⻉完成的⽂件数量
        count = 0
        while True:
            # 从队列中获取消息，如果取不到将阻塞
            queue.get()
            count += 1
            print("\r 当前进度是%% %f" % (100 * count * 1.0 / len(file_list)), end="")
            # ⽂件拷⻉完成 退出
            if count == len(file_list):
                break