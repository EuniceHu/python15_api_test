import requests

# 请求类
class HttpRequest(object):

    def http_request(self, url, param, http_method):

        if http_method == "GET":

            try:
                res = requests.get(url, param)
            except Exception as e:
                print(e)

        else:
            try:
                res = requests.post(url, param)

            except Exception as e:
                print(e)

        return res


if __name__ == '__main__':
    url = "http://47.107.168.87:8080/futureloan/mvc/api/member/login"

    param = {'mobilephone': '123', 'pwd': '123456'}

    res = HttpRequest().http_request(url, param, "POST")
    print(res.json())
    print(res.headers)
    print(res.status_code)
