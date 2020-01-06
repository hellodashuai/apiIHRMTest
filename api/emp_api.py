import requests
import app


class EmpApi:

    def __init__(self):
        self.emp_url = app.HOST + "/api/sys/user"
        # 注意:如果我们调用员工管理模块的相关接口时,先调用login.py接口
        # 获取到的app.DEADERS 才会是{"Content-Ttpe":"application","Authorization":"Bearer xxxx-xxx-xxxxx"}
        self.headers = app.HEADERS

    def add_emp(self, username, mobile):
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-01-10",
            "formOfEmployment": 2,
            "workNumber": "12323",
            "departmentName": "行政中心",
            "departmentId": "1066239766607040512",
            "correctionTime": "2020-01-14T16:00:00.000Z"
        }
        # 发送添加员工接口请求
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        # 返回添加员工接口的响应数据
        return response

    # 封装查询员工接口
    def query_emp(self):
        # 查询员工接口的url结构是http：//182.92.81.159/api/sys/user/12344344
        url = self.emp_url + '/' + app.EMP_ID
        # 返回查询的结果，headers是{'CONTENT-tYPE':'APPLICATION','Authorization':'Bearer xxx'}
        return requests.get(url, headers=self.headers)

    # 封装修改员工接口
    def modify_emp(self, username):
        # 修改员工的url应该和查询员工是一样的，所以拼接的时候也需要加上'/'
        # http://182.92.81.159/api/sys/user/1232142
        url = self.emp_url + '/' + app.EMP_ID
        # 从外部接收要修改的username，拼接成json数据
        data = {
            'username': username
        }
        # 返回查询结果
        return requests.put(url,
                            json=data,
                            headers=self.headers)

    # 封装删除员工接口
    def delete_emp(self):
        url = self.emp_url + '/' + app.EMP_ID
        # 调用删除的http接口并返回响应数据
        return requests.delete(url, headers=self.headers)
