# encoding=utf_8
# @Author  ： 豆子

import os

# 上2级目录
base_dir = os.path.dirname(os.path.dirname(__file__))

# configs目录
config_dir = os.path.join(base_dir, 'configs', 'log.conf')

# common文件目录
commons_dir = os.path.join(base_dir, 'commons')

# logs目录
log_dir = os.path.join(base_dir, 'logs')

# 测试报告目录
report_dir = os.path.join(base_dir, 'reports', 'report.html')

# 测试用例目录
case_dir = os.path.join(base_dir, 'test_case')

# 测试数据目录
data_dir = os.path.join(base_dir, 'test_data', 'test_data.xlsx')