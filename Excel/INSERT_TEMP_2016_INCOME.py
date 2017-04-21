# -*- coding: utf-8 -*-
# Author zfCode
import xlrd
from Oracle_helper import oracle_helper

h = oracle_helper('dsjky/quickhigh@192.168.2.105:1521/DSJKY')
data = xlrd.open_workbook('D:\\2016im.xls')
table = data.sheets()[0]
# print(len(data.sheets()))
nrows = table.nrows
ncols = table.ncols
# print(nrows,ncols)
for i in range(nrows):
    # print(table.row_values(i))
    # print(xlrd.xldate.xldate_as_datetime(table.row_values(i)[11], 0))
    # continue
    if str(table.row_values(i)[0]).find('/') > 0:
        traincode = table.row_values(i)[0].split("/")
        sql = '''
                INSERT INTO TB_TEMP_2016_INCOME (TRAIN_CODE, CB, SY,SR)
                VALUES ( N'%s', N'%s', N'%s', N'%s')
                ''' % (str(traincode[0]).strip()
                                     , round(float(str(table.row_values(i)[10]).replace('\xa0', '').strip()) / float(
            str(table.row_values(i)[6]).replace('\xa0', '').strip()), 2)
                                     , round(float(str(table.row_values(i)[15]).replace('\xa0', '').strip()) / float(
            str(table.row_values(i)[6]).replace('\xa0', '').strip()), 2)
                                     , round(float(str(table.row_values(i)[9]).replace('\xa0', '').strip()) / float(
            str(table.row_values(i)[6]).replace('\xa0', '').strip()), 2)
                       )
        print(sql)
        h.executeNoquery(sql)
        sql = '''
                INSERT INTO TB_TEMP_2016_INCOME (TRAIN_CODE, CB, SY,SR)
                VALUES ( N'%s', N'%s', N'%s', N'%s')
                ''' % (str(traincode[1]).strip()
                                     , round(float(str(table.row_values(i)[10]).replace('\xa0', '').strip()) / float(
            str(table.row_values(i)[6]).replace('\xa0', '').strip()), 2)
                                     , round(float(str(table.row_values(i)[15]).replace('\xa0', '').strip()) / float(
            str(table.row_values(i)[6]).replace('\xa0', '').strip()), 2)
                                     , round(float(str(table.row_values(i)[9]).replace('\xa0', '').strip()) / float(
            str(table.row_values(i)[6]).replace('\xa0', '').strip()), 2)
                       )
        print(sql)
        h.executeNoquery(sql)

    else:
        sql = '''
                       INSERT INTO TB_TEMP_2016_INCOME (TRAIN_CODE, CB, SY,SR)
                       VALUES ( N'%s', N'%s', N'%s', N'%s')
                       ''' % (str(table.row_values(i)[0]).replace('\xa0', '').strip()
                                            , round(
            float(str(table.row_values(i)[10]).replace('\xa0', '').strip()) / float(
                str(table.row_values(i)[6]).replace('\xa0', '').strip()), 2)
                                            , round(
            float(str(table.row_values(i)[15]).replace('\xa0', '').strip()) / float(
                str(table.row_values(i)[6]).replace('\xa0', '').strip()), 2)
                                            , round(
            float(str(table.row_values(i)[9]).replace('\xa0', '').strip()) / float(
                str(table.row_values(i)[6]).replace('\xa0', '').strip()), 2)
                              )
        print(sql)
        h.executeNoquery(sql)
