import smtplib

from conf import emailname, emailpwd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 总的邮件内容，分为不同的模块
msg_total = MIMEMultipart()
msg_total['Subject'] = 'hello'

# 正文模块
msg_raw = """<p style="color:red">你好</p>
"""
msg = MIMEText(msg_raw, 'html')
msg_total.attach(msg)

# 附件模块
mfile = MIMEApplication(open('demo.txt', 'rb').read())
# 添加附件的头信息
mfile.add_header('Content-Disposition', 'attachment', filename='demo')
# 附件摸快添加到总的里面
msg_total.attach(mfile)

with smtplib.SMTP_SSL('smtp.163.com', 465) as server:
    # 登录
    server.login(emailname, emailpwd)
    # msg = '''\\
    # From: yuze
    # Subject: test
    #
    # This is a test'''

    # 发送邮件
    server.sendmail(emailname, 'wagyu2016@163.com', msg_total.as_string())


    # 作业：新建一个类 class MyEmail, 完成带有附件的邮件发送。