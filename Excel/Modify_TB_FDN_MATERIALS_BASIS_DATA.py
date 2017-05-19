# -*- coding: utf-8 -*-
# Author zfCode
import xlrd
import datetime
from Oracle_helper import oracle_helper

h=oracle_helper('dsjky/quickhigh@192.168.2.105:1521/DSJKY')
data= xlrd.open_workbook('D:\公司文档\客运物资管理信息系统\文档\物资物料管理-料库名称对应关系（料库字典中料库名称-物资卡片中料库名称）.xlsx')
table = data.sheets()[1]
# print(len(data.sheets()))
nrows = table.nrows
ncols = table.ncols
print(nrows,ncols)
for i in range(nrows):
    sql='''
    update TB_FDN_MATERIALS_BASIS_DATA set CLKBM='%s' where CLKMC='%s';
    '''%(str(table.row_values(i)[3]).replace('\xa0','').strip(),str(table.row_values(i)[1]).replace('\xa0','').strip())



    print(sql)
    # h.executeNoquery(sql)
    # print(table.row_values(i))
