#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

# 买个电话当总机－接受客户端连接请求　转发到分机 ---> 服务器套接字或者监听套接字
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 使用固定号码 -- 使用固定端口
tcp_server.bind(('', 8888))

# 安装服务系统　设置等待服务区的大小 --- 默认的主动套接字设置为被动套接字
# 参数是 等待服务区(客户数量)的大小
tcp_server.listen(128)

while True:
    # 从等待服务区中 取出一个客户 用以服务 转接到分机之后 用分机进行服务
    #　　　　　　　　　　　　　　　　　　　　　　　　　　　　　分机　　　　　　　　　　　　　　　　　　　客户信息
    # accept没有参数 只有返回值 是一个元组(和客户端关联的套接字《通过该套接字可以和客户进行交流》, 客户端地址)
    client_socket, client_addr = tcp_server.accept()
    print("接收到来自%s 的连接请求" % str(client_addr))

    # 接收客户端的数据
    recv_data = client_socket.recv(4096)

    if recv_data:
        print("收到数据%s" % recv_data.decode())
        # 给客户端回数据
        client_socket.send(recv_data)
    else:
        print(recv_data)
        print("客户端已经断开ＴＣＰ连接")

        # 服务完成之后 分机挂掉
        client_socket.close()
        break

# 挂掉总机
# server_socket.close()
