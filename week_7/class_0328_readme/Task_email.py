#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Task_email.py
  @time: 2019/03/31
  
  """
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class MyEmail:
    def __init__(self,emailname,emailpwd,recv,title,
                 content,file=None,
                 email_host='smtp.163.com',
                 port=25
                 ):
        self.emailname=emailname
        self.emailpwd=emailpwd
        self.recv=recv#收件人的邮箱
        self.title=title
        self.content=content
        self.file=file
        self.email_host=email_host
        self.port=port
    def sendemail(self):
        #总的邮件内容，分为不同的模块
        msg_total=MIMEMultipart()
        msg_total['Subject']=self.title#邮件主题

        #正文模块
        msg_total.attach(MIMEText(self.content))

        #附件模块
        file=MIMEApplication(open(self.file,'rb').read())
        #添加附件的头信息
        file.add_header('Content-Disposition', 'attachment',filename=self.file)
        #附件内容添加到总的里面
        msg_total.attach(file)

        #邮件服务商
        server=smtplib.SMTP(self.email_host,self.port)

        #登录
        server.login(self.emailname,self.emailpwd)

        #发送邮件
        server.sendmail(self.emailname,self.recv,msg_total.as_string())
        def __del__(self):
            self.server.quit()


if __name__ == '__main__':
    em=MyEmail(emailname='hongdh1122@163.com',
            emailpwd='1992332211hdh',
            recv='hongdh1122@163.com',
            title='Hello',
            content='This is a test',
            file ='email.txt',
            email_host='smtp.163.com',
            port=25
            )
    em.sendemail()