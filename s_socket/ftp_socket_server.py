# Author:zfCode
import hashlib
import os
import socket
import json
import time


class FtpServer:
    def __init__(self):
        self.server = socket.socket()

    # 从服务端下载文件到客户端
    def get(self, conn, filename):
        if os.path.isfile(filename):
            f = open(filename, "rb")
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            msg_dic={
                "file_name": filename,
                "file_size": file_size
            }
            conn.send((json.dumps(msg_dic)).encode())

            conn.recv(1024)# 等待客户端反馈
            for line in f:
                m.update(line)
                conn.send(line)
            print("file md5:", m.hexdigest().encode())
        else:
            print(filename, "该文件不存在")

        print("send don")

    # 从客户端上传文件到服务端
    def put(self,filename):
        pass

    def cmd(self, conn, cmd_str):
        ret = os.popen(cmd_str)
        conn.send(ret.read().encode())

    def run(self, port):
        self.server.bind(('localhost', port))
        self.server.listen()
        print("listening...")
        while True:
            conn, addr = self.server.accept()
            print("new conn:", addr)
            data=conn.recv(1024)
            if not data:
                print("client was closed...")
                break

            msg_dic = json.loads(data.decode())
            if hasattr(self, msg_dic["action"]):
                func=getattr(self, msg_dic["action"])
                func(conn, msg_dic["filename"])
            else:
                print(msg_dic["action"],"not exist")





# server = socket.socket()
# server.bind(('localhost', 9999))
# server.listen()
# while True:
#     conn, addr = server.accept()
#     print("new conn:", addr)
#     while True:
#         print("等待新指令")
#         data = conn.recv(1024)
#         if not data:
#             print("客户端链接已断开")
#             break
#         cmd, filename = data.decode().split()
#         print(cmd,filename)
#         if os.path.isfile(filename):
#             f = open(filename, "rb")
#             m = hashlib.md5()
#             file_size = os.stat(filename).st_size
#             conn.send(str(file_size).encode())
#             conn.recv(1024)
#             for line in f:
#                 m.update(line)
#                 conn.send(line)
#             print("file md5:", m.hexdigest().endcode())
#         else:
#             print(filename, "该文件不存在")
#
#         print("send don")

server=FtpServer()
server.run(9999)

