import requests
from class_homework.unittest.test_logger import Logger


class Request:
    def request(self,method,url,param,cookies=None):

        if method.upper()=='GET':
            try:
                result=requests.get(url,param,cookies=cookies)
            except Exception as error:
                Logger().error('错误是:{}'.format(error))
                raise error

        elif method.upper()=='POST':
            try:
                result=requests.get(url,param,cookies=cookies)
            except Exception as error:
                Logger().error('错误是:{}'.format(error))
                raise error

        return result