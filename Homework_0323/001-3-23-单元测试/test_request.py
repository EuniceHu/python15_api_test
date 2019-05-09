import unittest
from http_request import HttpRequest
from ddt import ddt, data
from play_excel import PlayExcel

test_data = PlayExcel('http_request_data.xlsx','http_request_data').read_data()



@ddt
class TestRequest(unittest.TestCase):

    @data(*test_data)
    def test_001(self, item):
        print(item)
        res = HttpRequest().http_request(item['url'], eval(item['param']), item['http_method'])
        try:
            self.assertEqual(item['Expected'], eval(res.json()['code']))
        except AssertionError as e:
            raise e
        finally:
            print(res.json()['msg'])



if __name__ == '__main__':
    unittest.main()