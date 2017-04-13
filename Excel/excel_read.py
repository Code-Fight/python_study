# -*- coding: utf-8 -*-
# Author zfCode
import xlrd
from Oracle_helper import oracle_helper

h=oracle_helper('dsjky/quickhigh@192.168.2.105:1521/DSJKY')
data= xlrd.open_workbook('D:\\test.xls')
table = data.sheets()[0]
# print(len(data.sheets()))
nrows = table.nrows
ncols = table.ncols
# print(nrows,ncols)
for i in range(nrows):
    # print(table.row_values(i))
    # print(xlrd.xldate.xldate_as_datetime(table.row_values(i)[11], 0))
    # continue
    sql = '''
    INSERT INTO TB_TEMP_INTAKE (CJ, ZCBZ, ZCXM, KMBH, KMMC, YLDQ, CK, XDR, XDRQ, DKR, DKRQ, CKDH, WZBM, WZMC, GGXH, JLDW, CLFL, SL, KCDJ, JE)
    VALUES (N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s')
    '''%(str(table.row_values(i)[1]).replace('\xa0','').strip()
                   , str(table.row_values(i)[2]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[3]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[4]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[5]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[8]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[9]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[10]).replace('\xa0', '').strip()
                   , str(xlrd.xldate.xldate_as_datetime(table.row_values(i)[11], 0))
                   , str(table.row_values(i)[12]).replace('\xa0', '').strip()
                   , str(xlrd.xldate.xldate_as_datetime(table.row_values(i)[13], 0))
                   , str(table.row_values(i)[14]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[15]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[16]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[17]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[18]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[19]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[20]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[21]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[22]).replace('\xa0', '').strip()
         )
    print(sql)
    h.executeNoquery(sql)
    # print(table.row_values(i))
