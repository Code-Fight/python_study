# -*- coding: utf-8 -*-
# Author zfCode
import xlrd
import uuid
import datetime
from Oracle_helper import oracle_helper

h=oracle_helper('dsjky/quickhigh@192.168.2.105:1521/DSJKY')
data= xlrd.open_workbook('D:\公司文档\客运物资管理信息系统\文档\清家底\总表\客运系统物资清查表.xls')
print(data.sheets())
table = data.sheets()[1]
# print(len(data.sheets()))
nrows = table.nrows
ncols = table.ncols
print(nrows,ncols)


file_object = open('sql.txt', 'w+')
try:

    for i in range(nrows):

        # 仓库插入语句
        # sql='''
        # insert into RAILWAY.KY_JU_LOCATION(LOCATION_ID,LOCATION_NAME,LOCATION_STATION,LOCATION_TYPE,BUSINESS_CATEGORY,ITEM_ATTRIBUTE)
        # VALUES ('%s','%s','%s','STOREROOM','keyun','1');
        # '''%(str(table.row_values(i)[0]).replace('\xa0','').strip(),str(table.row_values(i)[1]).replace('\xa0','').strip(),
        # str(table.row_values(i)[2]).replace('\xa0', '').strip())

        # 物资卡片
        # sql='''
        # insert into RAILWAY.KY_JU_ITEM(itemnum,description,issueunit,c_Model,itemtype,create_Date,BUSINESS_CATEGORY,itemcategory,ROTATING)
        # VALUES ('%s','%s','%s','%s','ITEM',to_date('2017-5-19','yyyy-MM-dd'),'keyun','0','0');
        # '''%(str(table.row_values(i)[0]).replace('\xa0','').strip(),str(table.row_values(i)[1]).replace('\xa0','').strip(),
        # str(table.row_values(i)[2]).replace('\xa0', '').strip()
        #              , str(table.row_values(i)[3]).replace('\xa0', '').strip())


        # 库存主表--创效
        sql='''
        insert into RAILWAY.KY_JU_STOCK(STOCK_ID,STOCK_STATION,STOCK_LOCATION,STOCK_NUM,STOCK_NAME,STOCK_PRICE,STOCK_MAXNUM,STOCK_MINNUM
        ,BUSINESS_CATEGORY,STOCK_CURBAL,CONDITIONCODE,ITEM_ATTRIBUTE,CREATIVE)
        VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');
        '''%(uuid.uuid1(),
             str(table.row_values(i)[1]).replace('\xa0', '').strip(),
             '{:0>6}'.format((str(table.row_values(i)[2]).replace('.0', '').strip())),
             str(table.row_values(i)[3]).replace('\xa0', '').strip(),
             str(table.row_values(i)[4]).replace('\xa0', '').strip(),
             str(table.row_values(i)[7]).replace('\xa0', '').strip(),

             0,
             0,
             'keyun',
             str(table.row_values(i)[11]).replace('\xa0', '').strip(),
             '1',
             str(table.row_values(i)[24]).replace('\xa0', '').strip(),
             str(table.row_values(i)[25]).replace('\xa0', '').strip())


        # 库存子表
        # sql = '''
        #         insert into RAILWAY.KY_JU_STOCK_DETAIL(STOCK_DETAIL_ID,STOCK_ID,LOCATION,CURBAL,PRICE,MANUFACTURER_DATE,MANUFACTURER,LOCK_VERSION,CONDITIONCODE
        #         ,CREATE_DATE,AVAILABLE_NUM,BUSINESS_CATEGORY,ITEMNUM,LIFEPERIOD,QUALITY_DATE,STATION,ITEM_ATTRIBUTE)
        #         VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');
        #         ''' % (str(table.row_values(i)[0]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[1]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[2]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[3]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[4]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[5]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[6]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[7]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[8]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[9]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[10]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[11]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[12]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[13]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[14]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[15]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[16]).replace('\xa0', '').strip())


        # 库存子表
        # sql = '''
        #         insert into RAILWAY.KY_JU_STOCK_DETAIL(STOCK_DETAIL_ID,STOCK_ID,LOCATION,CURBAL,PRICE,CONDITIONCODE
        #         ,CREATE_DATE,AVAILABLE_NUM,BUSINESS_CATEGORY,ITEMNUM,STATION,ITEM_ATTRIBUTE,CREATIVE)
        #         VALUES ('%s','%s','%s','%s','%s','%s',to_date('%s','yyyy-MM-dd'),'%s','%s','%s','%s','%s','%s');
        #         ''' % (uuid.uuid1(),
        #                uuid.uuid1(),
        #                '{:0>6}'.format((str(table.row_values(i)[2]).replace('.0', '').strip())),
        #                str(table.row_values(i)[11]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[7]).replace('\xa0', '').strip(),
        #                '1',
        #
        #                '2017-05-31',
        #                str(table.row_values(i)[11]).replace('\xa0', '').strip(),
        #                'keyun',
        #                str(table.row_values(i)[3]).replace('\xa0', '').strip(),
        #
        #                str(table.row_values(i)[1]).replace('\xa0', '').strip(),
        #
        #                str(table.row_values(i)[24]).replace('\xa0', '').strip(),
        #                str(table.row_values(i)[25]).replace('\xa0', '').strip())

        file_object.write(sql)
finally:
        file_object.close()
        print("done...")









    # h.executeNoquery(sql)
    # print(table.row_values(i))
