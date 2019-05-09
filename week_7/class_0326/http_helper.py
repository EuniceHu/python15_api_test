

#!/usr/bin/python3

# Author:xuqiao

# Time:2019/3/2317:49

# File:htp_request.

# Email:1462942304@qq.com

import requests

class HttpGetPost:

    def http_request(self,url,method,data):

        if method.lower()=="get":

            return requests.get(url, params=data)

        elif method.lower()=="post":

            return requests.post(url,data=data)

        else:

            print("你输入的请求不对")

if __name__ == '__main__':

    res=HttpGetPost().http_request("http://47.107.168.87:8080/futureloan/mvc/api/member/login","post",{"mobilephone":18688773467, "pwd":123456})

    print(res.text)

    print(res.headers)

    print(res.status_code)

