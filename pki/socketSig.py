# -*- coding: utf-8 -*-

"""
@author: Franklin
@file: socketSig.py
@time: 2019/11/17 15:24
@dec: 
"""
 

import socket
# from pki import sm2
def socketClientA():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 6799))  # 绑定要监听的端口
    server.listen(5)  # 开始监听 表示可以使用五个链接排队
    while True:  # conn就是客户端链接过来而在服务端为期生成的一个链接实例
        conn, addr = server.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
        print(conn, addr)
        # while True:
        #     try:
        data = conn.recv(1024)  # 接收数据
        print('recive:', data.decode())  # 打印接收到的数据
        # conn.send(data.upper())  # 然后再发送数据
        # conn.close()
        # except ConnectionResetError as e:
        # print('关闭了正在占线的链接！')
        # break



def socketClientB():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 声明socket类型，同时生成链接对象
    client.connect(('localhost', 6799))  # 建立一个链接，连接到本地的6969端口

    while True:

        msg = "1.1.1.1.frank.1234"+ "-"+"42133b718ee607e50353d836dce6e2485421168495033c9563b9b123b5847f9294b2a2d29af91fec3963dcbb8e00fa27975b1935ebb1c00ddbef8118c98052dd"
        # sig = sm2.Sign()
        # addr = client.accept()
        # print '连接地址：', addr
        # msg = 'i am franklin！'  # strip默认取出字符串的头尾空格

        client.send(msg.encode('utf-8'))  # 发送一条信息 python3 只接收btye流
        data = client.recv(1024)  # 接收一个信息，并指定接收的大小 为1024字节
        print('recv:', data.decode())  # 输出我接收的信息
        # client.close()  # 关闭这个链接


if __name__ == "__main__":
    socketClientA()

