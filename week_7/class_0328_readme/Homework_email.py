#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Homework_email.py
  @time: 2019/03/31
  
  """
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from week_7.class_0328_readme import emailname,emailpwd

    #总的邮件内容，分为不同的模块
msg_total=MIMEMultipart()
msg_total['Subject']='hello'

    #正文模块
msg_raw = """<p style="color:red">你好</p>"""
msg=MIMEText(msg_raw,'html')
msg_total.attach(msg)

    #附件模块
file=MIMEApplication(open('email.txt','rb').read())
    #添加附件的头信息
file.add_header('Content-Disposition', 'attachment',filename='email.txt')
    #附件内容添加到总的里面
msg_total.attach(file)

    #邮件服务商
server=smtplib.SMTP('smtp.163.com',25)

    #登录
server.login(emailname,emailpwd)

    #发送邮件
    # msg = '''\\
    # From: xiaohu
    # Subject: test
    # Hello,this is a test'''

    #发送邮件
server.sendmail(emailname,'hongdh1122@163.com',msg_total.as_string())
server.quit()


# with smtplib.SMTP('smtp.163.com',25) as server:
#     # 登录
#     server.login(emailname, emailpwd)
#     # 发送邮件
#     msg = '''\\
#     From: xiaohu
#     Subject: test
#     Hello,this is a test'''
#
#     # 发送邮件
#     server.sendmail(emailname, 'hongdh1122@163.com', msg)


