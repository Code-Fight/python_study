# -*- coding: utf-8 -*-
# Author zfCode
import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

connection = cx_Oracle.connect('dsjky/quickhigh@192.168.2.105:1521/DSJKY')


cursor = cx_Oracle.Cursor(connection)  # 返回连接的游标对象


sql = "select * from TB_DIC_CITY"
cursor.execute(sql)
result = cursor.fetchall()
count = cursor.rowcount
print("=====================")
print("Total:", count)
print("=====================")
for row in result:
        print(row)
cursor.close()
connection.close()