# -*- coding: utf-8 -*-
# Author zfCode
from Oracle_helper import oracle_helper


h=oracle_helper("dsjky/quickhigh@192.168.2.105:1521/DSJKY")
sql = "select * from TB_DIC_CITY"

result = h.execute(sql)
count = len(result)
print("=====================")
print("Total:", count)
print("=====================")
for row in result:
    print(row)