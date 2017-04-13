# -*- coding: utf-8 -*-
# Author zfCode
import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class oracle_helper():
    def __init__(self, constr):
        # print(constr)
        # 建立链接
        self.connection = cx_Oracle.connect(constr)
        # 创建游标对象
        self.cursor = cx_Oracle.Cursor(self.connection)

    def cur(self):
        return self.cursor

    def executeData(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def executeNoquery(self, sql):
        temp= self.cursor.execute(sql)
        self.connection.commit();
        return temp


    def __del__(self):
        self.cursor.close()
        self.connection.close()


if __name__=="__main__":
    h=oracle_helper('dsjky/quickhigh@192.168.2.105:1521/DSJKY')
    sql = "select * from TB_DIC_CITY"

    result = h.execute(sql)
    count = len(result)
    print("=====================")
    print("Total:", count)
    print("=====================")
    for row in result:
        print(row)
