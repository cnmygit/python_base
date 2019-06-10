#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

# １　找个电话－－－创建套接字　和　服务器通信     流式报文
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 拨号 --- 建立和服务器的沟通渠道－连接　　参数就是服务器地址
server_ip = '192.168.101.20'
server_port = 8888
tcp_client.connect((server_ip, server_port))

# 3 交流－说听
# TCP中使用send()发送数据　只有一个参数就是需要发送的数据<bytes>
tcp_client.send('client,hello中国'.encode('utf-8'))

# 在ＴＣＰ中使用recv()接收数据　参数就是　本次接收数据的最大长度
# 返回值就是　　接收到的数据<bytes>
# recv会阻塞等待　直到数据到达　
recv_data = tcp_client.recv(4096)
print(recv_data.decode('utf-8'))

# ４　挂机  ---断开连接　释放套接字资源
tcp_client.close()