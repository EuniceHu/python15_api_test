"""
# 发送邮件
# 手工发邮件 ：
# 1选择邮件发送服务商，网易，qq
2. 登录
3. 编写邮件
4. 发送

# pop3 , smtp
"""

import smtplib
import ssl
# import poplib
from conf import emailname, emailpwd

# 邮件服务商 pyyaml .py   .ini  .conf
# server = smtplib.SMTP('smtp.163.com', 25)
#
# # 登录
# server.login(emailname, emailpwd)
#
# msg = '''\\
# From: yuze
# Subject: test
#
# This is a test'''
#
# # 发送邮件
# server.sendmail(emailname, 'wagyu2016@163.com', msg)
# server.quit()

context = ssl.create_default_context()


with smtplib.SMTP('smtp.163.com', 25) as server:
    # 登录
    server.login(emailname, emailpwd)
    server.starttls(context=context)
    msg = '''\\
    From: yuze
    Subject: test
    
    This is a test'''

    # 发送邮件
    server.sendmail(emailname, 'wagyu2016@163.com', msg)


# 加密， 重要情报 tls 模式

# 加密2， SSL  80 ==> 443    邮件 25==》 465
with smtplib.SMTP_SSL('smtp.163.com', 465) as server:
    # 登录
    server.login(emailname, emailpwd)
    msg = '''\\
    From: yuze
    Subject: test

    This is a test'''

    # 发送邮件
    server.sendmail(emailname, 'wagyu2016@163.com', msg)


# 添加附件 库 添加附件





