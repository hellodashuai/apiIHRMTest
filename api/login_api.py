import requests

import app


class LoginApi:
    def __init__(self):
        self.login_url = app.HOST + "/api/sys/login"
        self.headers = app.HEADERS
    # 从外部接受mobile和password
    # 为什么这么写?因为,如果写成一个参数data来接收

    def login(self,mobile,password):

        data = {
            "mobile":mobile,
            "password":password
        }

        response = requests.post(self.login_url,
                                 json=data,
                                 headers=self.headers)
        return response
