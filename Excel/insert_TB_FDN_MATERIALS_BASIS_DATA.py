# -*- coding: utf-8 -*-
# Author zfCode
import xlrd
from Oracle_helper import oracle_helper

h=oracle_helper('dsjky/quickhigh@192.168.2.105:1521/DSJKY')
data= xlrd.open_workbook('D:\公司文档\客运物资管理信息系统\物资系统2.0\物资2.0-各段上报信息\长春客运段物资卡片目录.doc.xls')
table = data.sheets()[0]
# print(len(data.sheets()))
nrows = table.nrows
ncols = table.ncols
print(nrows,ncols)
for i in range(nrows):
    # print(table.row_values(i))
    # print(xlrd.xldate.xldate_as_datetime(table.row_values(i)[21], 0))
    # continue

    print(table.row_values(i)[20])


    sql='''Insert into DSJKY.TB_FDN_MATERIALS_BASIS_DATA (
        DW,CJ,CLKMC,WZBH,WZMC,GGXH,JLDW,KCDJ,QC_COUNT,SR_COUNT,
        ZC_COUNT,QM_COUNT,QC_MONEY,SR_MONEY,ZC_MONEY,QM_MONEY,SCCJ,CCRQ,ZBQ,SMQX,
        CLFL,STATE,MAX_CBDL,MIN_CBDL,WZSX,BFSJ,BFGZ,TIME)
VALUES (N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s',
        N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s',to_date('%s','yyyy-MM-dd'), to_date('%s','yyyy-MM-dd'),to_date('%s','yyyy-MM-dd'),
        N'%s', N'%s', N'%s', N'%s', N'%s',to_date('%s','yyyy-MM-dd'), N'%s', to_date('%s','yyyyMM') )
    '''%(str(table.row_values(i)[17]).replace('\xa0','').strip()
                   , str(table.row_values(i)[18]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[2]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[4]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[5]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[6]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[7]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[8]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[9]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[11]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[13]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[15]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[10]).replace('\xa0', '').strip()
                   , str(table.row_values(i)[12]).replace('\xa0', '').strip()
                 , str(table.row_values(i)[14]).replace('\xa0', '').strip()
                 , str(table.row_values(i)[16]).replace('\xa0', '').strip()
                 , str(table.row_values(i)[19]).replace('\xa0', '').strip()
                 , xlrd.xldate.xldate_as_datetime(table.row_values(i)[20], 0).strftime('%Y-%m-%d') if len(str(table.row_values(i)[20]).replace('\xa0', '').strip())>0 else ""
                 ,  xlrd.xldate.xldate_as_datetime(table.row_values(i)[21], 0).strftime('%Y-%m-%d') if len(str(table.row_values(i)[21]).replace('\xa0', '').strip())>0 else ""
                 , xlrd.xldate.xldate_as_datetime(table.row_values(i)[22], 0).strftime('%Y-%m-%d') if len(str(table.row_values(i)[22]).replace('\xa0', '').strip())>0 else ""
                 , str(table.row_values(i)[23]).replace('\xa0', '').strip()
                 , str(table.row_values(i)[24]).replace('\xa0', '').strip()
                 , str(table.row_values(i)[25]).replace('\xa0', '').strip()
                 , str(table.row_values(i)[26]).replace('\xa0', '').strip()
                 , str(table.row_values(i)[27]).replace('\xa0', '').strip()
                 ,xlrd.xldate.xldate_as_datetime(table.row_values(i)[28], 0).strftime('%Y-%m-%d') if len(str(table.row_values(i)[28]).replace('\xa0', '').strip())>0 else ""
                 , str(table.row_values(i)[29]).replace('\xa0', '').strip()
                 , str(table.row_values(i)[3]).replace('\xa0', '').strip()
         )


    # sql = '''
    # INSERT INTO TB_FDN_MATERIALS_BASIS_DATA (DW, CLKMC, WZBH, WZMC, GGXH,JLDW,KCDJ,QC_COUNT,SR_COUNT,ZC_COUNT,QM_COUNT,QC_MONEY,SR_MONEY,ZC_MONEY,QM_MONEY)
    # VALUES (N'吉林客运段', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s')
    # '''%(str(table.row_values(i)[2]).replace('\xa0','').strip()
    #                , str(table.row_values(i)[4]).replace('\xa0', '').strip()
    #                , str(table.row_values(i)[5]).replace('\xa0', '').strip()
    #                , str(table.row_values(i)[6]).replace('\xa0', '').strip()
    #                , str(table.row_values(i)[7]).replace('\xa0', '').strip()
    #                , str(table.row_values(i)[8]).replace('\xa0', '').strip()
    #                , str(table.row_values(i)[9]).replace('\xa0', '').strip()
    #                , str(table.row_values(i)[11]).replace('\xa0', '').strip()
    #                , str(table.row_values(i)[13]).replace('\xa0', '').strip()
    #                , str(table.row_values(i)[15]).replace('\xa0', '').strip()
    #                , str(table.row_values(i)[10]).replace('\xa0', '').strip()
    #                , str(table.row_values(i)[12]).replace('\xa0', '').strip()
    #                , str(table.row_values(i)[14]).replace('\xa0', '').strip()
    #                , str(table.row_values(i)[16]).replace('\xa0', '').strip()
    #      )
    print(sql)
    h.executeNoquery(sql)
    # print(table.row_values(i))
