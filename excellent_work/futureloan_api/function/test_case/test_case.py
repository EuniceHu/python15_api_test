# -*- coding: utf-8 -*-
# @Author  : hubing   
# @mail    : cocofei-f@163.com
# @Date    : 2019-04-15 17:21
from function.commons.excel_process import ExcelProcess
from function.commons import file_path

class TestCase():

    def __init__(self):
        self.case_id = None
        self.title = None
        self.url = None
        self.data = None
        self.method = None
        self.expected = None
        self.actual = None
        self.result = None

import json
class ToExcel(ExcelProcess):

    def read_excel_sheet_by_dict(self,sheetName):
        sheet = self.wb[sheetName]
        max_row = sheet.max_row

        data_list = []
        for r in range(2,max_row+1):
            testCase = TestCase()
            testCase.case_id = sheet.cell(row=r,column=1).value
            testCase.title = sheet.cell(row=r, column=2).value
            testCase.url = sheet.cell(row=r, column=3).value
            testCase.data = eval(sheet.cell(row=r, column=4).value)
            testCase.method = sheet.cell(row=r, column=5).value
            testCase.expected = sheet.cell(row=r, column=6).value
            testCase.actual = sheet.cell(row=r, column=7).value
            testCase.result = sheet.cell(row=r, column=8).value

            data_list.append(testCase)
        self.close()
        return data_list



if __name__ == '__main__':
    toexcel = ToExcel(r'D:\python\futureloan_api\data\futureloan_cases.xlsx')
    case = toexcel.read_excel_sheet_by_dict(sheetName='login')
    for i in case:
        # print(json.loads(i.data))
        a = i.data
        print(i.__dict__)
    #
    # params = '{"mobilephone": "13480166986", "pwd": "123456", "regname": "胡兵"}'
    # params = '{"mobilephone": "15919872234", "pwd": "0callwo-bcdehubing", "regname": "胡兵"}'
    # params = '{"mobilephone": "18607353918", "pwd": "a123456789", "regname": None}'
    # params = '{"mobilephone": "18607353918", "pwd": None, "regname": None}'
    # params = '{"mobilephone": "1348016698", "pwd": 123456, "regname": None}'
    # params = '{"mobilephone": "18607353918", "pwd": None, "regname": None}'
    # params = '{"mobilephone": "28607353918", "pwd": None, "regname": None}'
    # params = '{"mobilephone": None, "pwd": 123456, "regname": "胡兵"}'
    # params = '{"mobilephone": 18607353919, "pwd": 12345, "regname": "胡兵"}'
    # params = '{"mobilephone": 18607353920, "pwd": "abcdefghijk123456789", "regname": "胡兵"}'
    # params = '{"mobilephone": "13480166986", "pwd": "123456", "regname": "胡兵"}'
    # #
    # # params = '{"mobilephone":"18607353918","pwd":"a123456789","regname":None}'
    # j = eval(params)
    # print(type(j),j)