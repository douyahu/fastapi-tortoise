# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：Email.py
@IDE ：PyCharm
"""
import os
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailService(object):

    def __init__(self, host, port, is_ssl, username, password, default_sender):
        self.host = host
        self.port = port
        self.is_ssl = is_ssl
        self.username = username
        self.password = password
        self.default_sender = default_sender

    def send_email(self, subject, receivers, content, attach_files=[]):
        '''
            以读取文件的方式加载附件，再发送邮件
        :param subject:邮件标题
        :param receivers:接收人
        :param content:邮件正文
        :param attach_files:附件
        :return:
        '''
        encoding = 'utf-8'
        m = MIMEMultipart()
        message = MIMEText(content, 'plain', encoding)
        m.attach(message)
        m['From'] = Header(self.default_sender, encoding)
        m['To'] = ';'.join([receivers])
        m['Subject'] = Header(subject, encoding)
        # 添加附件
        for file in attach_files:
            with open(file, 'r', encoding='UTF-8') as f:
                attach_apart = MIMEApplication(f.read())
                attach_apart.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                m.attach(attach_apart)
        if self.is_ssl:
            smtp = smtplib.SMTP_SSL(self.host, self.port, timeout=10)
            smtp.ehlo()
        else:
            smtp = smtplib.SMTP(self.host, self.port, timeout=10)
            smtp.ehlo()
        if self.password:
            smtp.login(self.username, self.password)
        smtp.sendmail(self.default_sender, receivers, m.as_string())
