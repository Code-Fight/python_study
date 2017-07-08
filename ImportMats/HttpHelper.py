# -*- coding: utf-8 -*-
# Author zfCode
import urllib
import json
import urllib.request
import http.cookiejar

class Http:
    def __init__(self):
        # self.url="http://10.32.112.165/railway_material/m3/pubWebservice.do"
        # self.host = host
        # self.url = host+"/WebHandler/AJAX.ashx?type=AjaxDepartmentManage&method=AddDepartment&Instance=undefined"
        # self.url = host
        # self.proxy_support = urllib.request.ProxyHandler({"http": "http://quickhigh:quickhigh@223.100.134.235:808/"})
        # self.proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
        # self.opener = urllib.request.build_opener(self.proxy_support)
        # urllib.request.install_opener(self.opener)
        cookie_filename = 'cookie.txt'
        self.cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
        handler = urllib.request.HTTPCookieProcessor(self.cookie)
        cookopener = urllib.request.build_opener(handler)
        urllib.request.install_opener(cookopener)

    def Post(self, url, postdata):
        try:
            if len(url) == 0:
                return
            self.url = url
            data = urllib.parse.urlencode(postdata)
            data = data.encode(encoding='UTF8')
            response = urllib.request.urlopen(self.url, data)
            the_page = response.read()
            self.cookie.save(ignore_discard=True, ignore_expires=True)
            # print(self.cookie)
            return the_page.decode("UTF-8")
        except urllib.error.HTTPError as e:
            print('--------------error--------------')
            print(e.code)
            print(e.info())
            print(e.geturl())
            print(e.read())

    def Get(self, url, params):
        try:
            if len(url) == 0:
                return
            self.url = url
            data = urllib.parse.urlencode(params)
            # data = json.dumps(params)
            print(data)
            data=data.encode(encoding='UTF8')
            # req = urllib.request.Request(self.url+'?'+params)
            # response = urllib.request.urlopen(self.url+"?data="+data)
            response = urllib.request.urlopen(self.url, data)
            the_page = response.read()
            self.cookie.save(ignore_discard=True, ignore_expires=True)
            return the_page.decode("UTF-8")
        except urllib.error.HTTPError as e:
            print('--------------error--------------')
            print(e.code)
            print(e.info())
            print(e.geturl())
            print(e.read())




if __name__=="__main__":

    ''''
    IsAdded=true&deptcode=&deptname=test&dept_type_name=%E8%BD%A6%E9%98%9F&dept_type_code=10814&parentcode=DEPT000073&seqvalue=1&activated=checked&description='''

    # print(urllib.request.urlopen('''http://10.32.112.165/railway_material/m3/pubWebservice.do?data={"data": [{"param": "KyJuDept", "data": [{"deptName": "\u4ed3\u5e93\u540d\u79f0", "parentDeptId": "1.1", "stationId": "1", "deptCode": "1", "businessCategory": "gw", "deptTypeId": "1", "deptId": "1"}], "pkId": " deptId "}], "method": "saveReturnDataParam", "type": "1"}''').read().decode("UTF-8"))
    params={
        'Action' : 'Login' ,
        'username' : 'sa' ,
        'password' : 'qhquickhigh'
    }

    deptParams= {
        'IsAdded': 'true',
        'deptcode': '',
        'deptname': '这是post测试车队',
        'dept_type_name': '车队',
        'dept_type_code': '10814',
        'parentcode': 'DEPT000073',
        'seqvalue': '1',
        'activated': 'checked',
        'description': ''

    }
    H=Http()
    ret = H.Post('http://localhost:61587/WebHandler/ValiDate.ashx', params)

    ret = H.Post('http://localhost:61587/WebHandler/AJAX.ashx?type=AjaxDepartmentManage&method=AddDepartment&Instance=undefined', deptParams)
    print(json.loads(ret)["Message"])
    # print(ret["Message"])
    # if str(ret).find('成功'):
    #     print("插入成功")
    # else:
    #     print(ret["Message"])
    # ret=H.Post("browser=mozilla%2F5.0+(windows+nt+10.0%3B+win64%3B+x64)+applewebkit%2F537.36+(khtml%2C+like+gecko)+chrome%2F59.0.3071.115+safari%2F537.36")
    # H = Http("http://localhost:61587/Index.aspx")
    # print(ret)