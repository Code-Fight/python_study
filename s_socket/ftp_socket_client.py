# Author:zfCode
import socket
import json
import os


class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    def help(self):
        msg = '''
        ls/dir
        pwd
        cd ../..
        get filename
        put filename
        '''
        print(msg)

    def connect(self, ip, port):
        self.client.connect((ip, port))

    def interactive(self):
        while True:
            cmd = input(">>").strip()
            if len(cmd) == 0: continue
            cmd_str = cmd.split()[0]
            if hasattr(self, 'cmd_%s' % cmd_str):
                func = getattr(self, 'cmd_%s' % cmd_str)
                func(cmd)
            else:
                self.help()

    def cmd_put(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            filesize = os.stat(filename).st_size
            msg_dic = {
                "action": "put",
                "filename": filename,
                "filesize": filesize,
                "overridden": True
            }
            self.client.send((json.dumps(msg_dic)).encode("utf-8"))
            print("send", (json.dumps(msg_dic)).encode("utf-8"))

            # 防止粘包 等服务器确认
            server_response = self.client.recv(1024)
            f = open(filename, "rb")
            for line in f:
                self.client.send(line)
            else:
                print(filename, "is not exist")

    def cmd_get(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if len(cmd_split) > 2:
                new_filename = cmd_split[2]
            else:
                # 获取新文件名 如果没有设置就默认采用 原文件名+_new
                new_filename = filename.split('.')[0] + "_new" + "." + filename.split('.')[1]
            msg_dic = {
                "action": "get",
                "filename": filename
            }
            self.client.send(json.dumps(msg_dic).encode())
            server_response = self.client.recv(1024)  # 这里服务器返回一个dic 包含文件信息
            print("server response:", server_response)
            server_response_dic=json.loads(server_response.decode())
            self.client.send(str("ready to recv file").encode())
            # TODO:这下面应该解包json反馈的数据 得到文件大小 以及文件信息 等 最后循环接收数据 并且写入到文件中
            file_total_size = int(server_response_dic["file_size"])
            received_size = 0
            f= open(new_filename, "wb")
            while received_size < file_total_size:
                data = self.client.recv(1024)
                received_size += len(data)
                f.write(data)
            else:
                print("file recv done", received_size, file_total_size)
                f.close()

            '''
            file_total_size = int(server_response.decode())
             received_size = 0
            filename = cmd.split()[1]
            f = open(filename + ".new","wb")
       while received_size < file_total_size:
         data = client.recv(1024)
         received_size += len(data)
         f.write(data)
         #print(file_total_size,received_size)
       else:
         print("file recv done", received_size,file_total_size)
         f.close()
         '''


ftp = FtpClient()
ftp.connect("localhost", 9999)
ftp.interactive()
