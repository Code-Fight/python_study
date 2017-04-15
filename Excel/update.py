# -*- coding: utf-8 -*-
# Author zfCode

import xlrd
import random
import datetime
from Oracle_helper import oracle_helper

h=oracle_helper('dsjky/quickhigh@192.168.2.105:1521/DSJKY')

# data= xlrd.open_workbook('D:\\excel\\wuzikapian.xls')
table = h.executeData("select * from TB_FDN_MATERIALS_BASIS_DATA")
dw=h.executeData("select ZCBZ from TB_TEMP_INTAKE group by ZCBZ")
d = datetime.datetime.now()
# random_d = d + datetime.timedelta(days=-random.randrange(20,100))




# nrows = table.nrows
# ncols = table.ncols
# for i in table:
#     index = random.randrange(0, len(dw) - 1)
#     print(dw[index][0])
#     sql="update TB_FDN_MATERIALS_BASIS_DATA set SCCJ=N'%s' where ID='%s'"%(dw[index][0],i[0])
#     print(sql)
#     h.executeNoquery(sql)
#
for i in table:
    index = random.randrange(0, len(dw) - 1)
    # print(dw[index][0])
    random_d = d + datetime.timedelta(days=-random.randrange(20, 100))
    random_l = random_d + datetime.timedelta(days=random.randrange(200, 500))
    random_z = random_l + datetime.timedelta(days=random.randrange(200, 500))
    # print(random_d.date())
    sql="update TB_FDN_MATERIALS_BASIS_DATA set CCRQ=to_date('%s','yyyy-MM-dd'),ZBQ=to_date('%s','yyyy-MM-dd'),SMQX=to_date('%s','yyyy-MM-dd'),CLFL=N'材料',STATE=N'良好',MAX_CBDL=N'%s',MIN_CBDL=N'%s',WZSX=N'账内保管',BFSJ=to_date('%s','yyyy-MM-dd'),BFGZ=N'' where ID='%s'"\
        %(random_d.date(),random_l.date(),random_z.date(),(random.randrange(2,8)*100),(random.randrange(11,20)*1000),random_z.date(),i[0])
    print(sql)
    h.executeNoquery(sql)

# for j in dw:
#     index=random.randrange(0,len(dw)-1)
#     print(index)
#     print(dw[index])



