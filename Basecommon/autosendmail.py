'''
Created on 2019年5月16日
@author: king
@job number:xy04952
'''
# coding:utf-8

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser
import time


class Sendmail:
    def __init__(self):
        self.date=time.strftime("%Y-%m-%d_%H_%M_%S")
        config=configparser.ConfigParser()
        config.read('E:\\pythonscript\\xkw.zxxk\\conf\\data.conf', 'utf-8')
        self.sender=config.get("UserEmail","sender")
        self.receiver=config.get("UserEmail","receiver")
        self.smtpserver=config.get("UserEmail","smtpserver")
        self.username=config.get("UserEmail","username")
        self.password=config.get("UserEmail","password")
        self.sender=config.get("UserEmail","sender")
        self.mail_title = self.date+'学科网首页自动化测试报告'
    
    #发送邮件
    def sendEmail(self,file,reportfile):
        
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = self.receiver
        message['Subject'] = Header(self.mail_title, 'utf-8')
 
        # 邮件附件
        #message.attach(MIMEText('学科网自动化回归测试结果', 'plain', 'utf-8'))
        f=open(file,'rb')
        mail_body=f.read()
        f.close()
        msg_html1 = MIMEText(mail_body,'html','utf-8')
        message.attach(msg_html1)
    
        msg_html = MIMEText(mail_body,'html','utf-8')
        msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        message.attach(msg_html)
         
        #邮件正文
        att = MIMEText(open(file,'rb').read(),'base64','utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename='+file
        message.attach(att)

        smtpObj = smtplib.SMTP_SSL(self.smtpserver)
        smtpObj.connect(self.smtpserver,'465')
        smtpObj.login(self.username, self.password)
        smtpObj.sendmail(self.sender, self.receiver, message.as_string())
        print("\n邮件发送成功！！！")
        smtpObj.quit()

sendmail=Sendmail()