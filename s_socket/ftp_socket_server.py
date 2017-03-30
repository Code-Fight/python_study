# Author:zfCode
import hashlib
import os
import socket
import time

server = socket.socket()
server.bind(('0,0,0,0', 9999))
server.listen()

while True:
    conn, addr = server.accept()
    print("new conn:", addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端链接已断开")
            break
        cmd, filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f = open(filename, "rb")
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())
            conn.recv(1024)
            for line in f:
                m.update(line)
                conn.send(line)
            print("file md5:", m.hexdigest().endcode())
        else:
            print(filename, "该文件不存在")

        print("send don")

server.colse()
