# -*- coding: utf-8 -*-
# Author zfCode
import HttpHelper
import json
import xlrd
import OracleHelper

# base params
FilePath = 'D:\公司文档\客运物资管理信息系统\各站段基础数据\import.xlsx'
# item in sheet 0
sheet = 6
orcale = OracleHelper.Oracle('mat/quickhigh@192.168.2.105:1521/MATTEST')


params={
        'Action' : 'Login',
        'username' : 'sa',
        'password' : 'qhquickhigh'
    }



def ReadExcel():
    ExcelData = xlrd.open_workbook(FilePath)
    table = ExcelData.sheets()[sheet]
    nrows = table.nrows
    ncols = table.ncols
    print('rows：%s  | cols: %s' % (nrows, ncols))
    return table




def CreatSql():
    pass

def Start():
    table = ReadExcel()
    H = HttpHelper.Http()
    ret = H.Post('http://192.168.2.201:20112/WebHandler/ValiDate.ashx', params)
    # file_object = open('items_sql.txt', 'w+', encoding="utf-8")

    if table.nrows > 0:
        # 先验证段是否存在
        duan_code = str(table.row_values(1)[2]).replace('\xa0', '').strip()
        if len(duan_code) == 0:
            print("请填写段信息")
            return
        duan = orcale.ExecuteData("select * from TB_AUT_DEPARTMENT where DEPTCODE='%s'" % (
            str(table.row_values(1)[2]).replace('\xa0', '').strip()
        ))
        if len(duan) == 0:
            print("段不存在")
            return
    else:
        print("not data!")
    lastDept = ""
    try:
        for i in range(table.nrows - 1):
            if str(table.row_values(i + 1)[1]).replace('\xa0', '').strip() != lastDept:
                lastDept = str(table.row_values(i + 1)[1]).replace('\xa0', '').strip()
                # 查找是已经存在车队
                dept = orcale.ExecuteData("select * from TB_AUT_DEPARTMENT where Parentcode='%s' and Deptname='%s'"% (
                    duan_code,
                    lastDept
                ))


            if len(dept)== 0:
                # 先创建车队
                deptParams = {
                    'IsAdded': 'true',
                    'deptcode': '',
                    'deptname': lastDept,
                    'dept_type_name': '车队',
                    'dept_type_code': '10814',
                    'parentcode': duan_code,
                    'seqvalue': '0',
                    'activated': 'checked',
                    'description': ''
                }
                ret = H.Post(
                    'http://192.168.2.201:20112/WebHandler/AJAX.ashx?type=AjaxDepartmentManage&method=AddDepartment&Instance=undefined',
                    deptParams)
                # print(json.loads(ret)["Message"])
                if str(json.loads(ret)["Message"]).find("成功"):
                    print(lastDept+" 插入成功")
                    dept = orcale.ExecuteData(
                        "select * from TB_AUT_DEPARTMENT where Parentcode='%s' and Deptname='%s'" % (
                            duan_code,
                            lastDept
                        ))

                else:
                    print(lastDept+" 插入失败")
                    return
            # print("车队信息：" + dept[0][0])
            # 开始创建班组
            deptParams = {
                'IsAdded': 'true',
                'deptcode': '',
                'deptname': str(table.row_values(i + 1)[0]).replace('\xa0', '').strip().replace('.0', ''),
                'dept_type_name': '班组',
                'dept_type_code': '10815',
                'parentcode': dept[0][0],
                'seqvalue': '0',
                'activated': 'checked',
                'description': ''
            }
            ret = H.Post(
                'http://192.168.2.201:20112/WebHandler/AJAX.ashx?type=AjaxDepartmentManage&method=AddDepartment&Instance=undefined',
                deptParams)
            if str(json.loads(ret)["Message"]).find("成功") > 0:
                print(str(table.row_values(i + 1)[0]).replace('\xa0', '').strip().replace('.0', '') + " 插入成功")
            elif str(json.loads(ret)["Message"]).find("存在") > 0:
                print(str(table.row_values(i + 1)[0]).replace('\xa0', '').strip().replace('.0', '') + " 已经存在")
            else:
                print(str(table.row_values(i + 1)[0]).replace('\xa0', '').strip().replace('.0', '') + " 插入失败")
                return

    finally:
        pass
        # file_object.close()
        # print("done...")



if __name__ == '__main__':
    Start()