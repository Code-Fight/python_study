# -*- coding: utf-8 -*-
# Author zfCode
import xlrd
import OracleHelper

# base params
FilePath = 'D:\公司文档\客运物资管理信息系统\各站段基础数据\import.xlsx'
# item in sheet 0
sheet = 0

item_type = {
    "消耗品": "64001",
    "备品": "64002"
}
# 0材料、1燃料、2配件、3工具仪表、4设备、5办公用品、6劳保用品
item_category = {
    "材料": "0",
    "燃料": "1",
    "配件": "2",
    "工具仪表": "3",
    "设备": "4",
    "办公用品": "5",
    "劳保用品": "6"
}

# methods
def ReadExcel():
    ExcelData = xlrd.open_workbook(FilePath)
    table = ExcelData.sheets()[sheet]
    nrows = table.nrows
    ncols = table.ncols
    print('rows：%s  | cols: %s' % (nrows, ncols))
    return table


def ReadDb():
    orcale = OracleHelper.Oracle('dsjky/quickhigh@192.168.2.105:1521/DSJKY_P')
    ret = orcale.ExecuteData("select * from TB_FDN_MATERIALS_CARD")

def CreatSql():
    pass

def Start():
    table = ReadExcel()
    file_object = open('items_sql.txt', 'w+',encoding="utf-8")
    try:
        for i in range(table.nrows-1):
            sql='''
            insert into TB_FDN_MATERIALS_CARD(WZM,WZBM,GGXH,JLDW,HSDJ,WZLB_CODE,WZLB_NAME,ITEMCATEGORY,XXJS,MAX,MIN,GSDW_CODE,GSDW_NAME)VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');
            '''%(
                str(table.row_values(i+1)[0]).replace('\xa0', '').strip(),
                str(table.row_values(i+1)[1]).replace('\xa0', '').strip(),
                str(table.row_values(i+1)[2]).replace('\xa0', '').strip(),
                str(table.row_values(i+1)[3]).replace('\xa0', '').strip(),
                str(table.row_values(i+1)[4]).replace('\xa0', '').strip(),
                item_type[str(table.row_values(i+1)[5]).replace('\xa0', '').strip()],
                str(table.row_values(i+1)[5]).replace('\xa0', '').strip(),
                item_category[str(table.row_values(i+1)[6]).replace('\xa0', '').strip()],
                str(table.row_values(i+1)[7]).replace('\xa0', '').strip(),
                str(table.row_values(i+1)[8]).replace('\xa0', '').strip(),
                str(table.row_values(i+1)[9]).replace('\xa0', '').strip(),
                str(table.row_values(i+1)[10]).replace('\xa0', '').strip(),
                str(table.row_values(i+1)[11]).replace('\xa0', '').strip()
            )

            file_object.write(sql)
            print("writing...  | ", i+1)
    finally:
        file_object.close()
        print("done...")

if __name__ == '__main__':
    Start()
