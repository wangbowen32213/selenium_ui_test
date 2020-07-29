#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
from tools.logger import log
sys.path.append('.')
import zmail
from config.conf import REPORT_PATH, EMAIL_INFO, ADDRESSEE


def send_report():
    """发送报告"""
    with open(REPORT_PATH, encoding='utf-8') as f:
        content_html = f.read()
    try:
        mail = {
            'from': 'wbw19930822@163.com',
            'subject': '最新的测试报告邮件',
            'content_html': content_html,
            'attachments': [REPORT_PATH, ]
        }
        server = zmail.server(*EMAIL_INFO.values())
        server.send_mail(ADDRESSEE, mail)
    except Exception as e:
        print("Error: 无法发送邮件，{}！", format(e))
        # log.info("Error: 无法发送邮件，{}！", format(e))
    else:
        print("测试邮件发送成功！")
        # log.info("发送成功")


if __name__ == "__main__":
    send_report()

# import sys
#
# sys.path.append('.')
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from config.conf import REPORT_PATH, EMAIL_INFO, ADDRESSEE
# import os
# import sys
# sys.path.append("..")
# def send_email():
#     file_path = REPORT_PATH
#     sendfile = open(file_path , 'rb').read()
#
#     att = MIMEText(sendfile,'base64','utf-8')
#     att['Content-Type'] = 'application/octet-stream'
#     att['Content-Disposition'] = 'attachment; filename="report.html"'
#
#     msgRoot = MIMEMultipart('related')
#
#     msgRoot['Subject'] = "测试报告"
#     msgRoot.attach(att)
#
#     smtp = smtplib.SMTP()
#     try:
#         smtp.connect(EMAIL_INFO['smtp_host'])
#         smtp.login(EMAIL_INFO['username'],EMAIL_INFO['password'])
#         smtp.sendmail(EMAIL_INFO['username'],ADDRESSEE[-1],msgRoot.as_string())
#         print("成功")
#     except Exception as e:
#         print(e)
#         print("Error 失败")
#     finally:
#         smtp.quit()
#
# def report_file():
#
#     #定义文件目录
#     result_dit = REPORT_PATH
#
#     lists = os.listdir(result_dit)
#
#     #按照时间对文件进行排序
#     lists.sort(key=lambda fn: os.path.getatime(result_dit+"\\" + fn))
#
#     # print(lists[-1])
#
#     file = os.path.join(result_dit,lists[-1])
#
#     return file
#
#
# if __name__ == '__main__':
#     send_email()
#     # print(REPORT_PATH)