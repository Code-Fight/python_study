# -*- coding: utf-8 -*-
# Author zfCode
import xlrd
from Oracle_helper import oracle_helper

h=oracle_helper('dsjky/quickhigh@192.168.2.105:1521/DSJKY')
data= xlrd.open_workbook('D:\公司文档\客运物资管理信息系统\物资系统2.0\物资卡片目录_0508.xls')
table = data.sheets()[0]
# print(len(data.sheets()))
nrows = table.nrows
ncols = table.ncols
# print(nrows,ncols)
for i in range(nrows):
    # print(table.row_values(i))
    # print(xlrd.xldate.xldate_as_datetime(table.row_values(i)[11], 0))
    # continue

    wzbm=str(table.row_values(i)[4]).replace('\xa0', '').strip()
    type_code=''
    type_name=''
    if wzbm[0:2]=="01":
        type_code = '64001'
        type_name = '消耗品'
    else:
        type_code = '64002'
        type_name = '备品'

    sql = '''
    INSERT INTO TB_FDN_MATERIALS_CARD (WZM, WZBM, GGXH, JLDW, HSDJ,WZLB_CODE,WZLB_NAME)
    VALUES (N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s')
    '''%(str(table.row_values(i)[5]).replace('\xa0','').strip()
                   , str(table.row_values(i)[4]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[6]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[7]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[8]).replace('\xa0', '').strip()
                   , type_code
                   , type_name
         )
    print(sql)
    h.executeNoquery(sql)
    # print(table.row_values(i))
