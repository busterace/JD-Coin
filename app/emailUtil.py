#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

' a email module '

__author__ = 'busterace'


def send(content):
    msg_from = '308578867@qq.com'  # 发送方邮箱
    passwd = 'aalewzhrsdzjbige'  # 填入发送方邮箱的授权码
    msg_to = '308578867@qq.com'  # 收件人邮箱

    subject = "京东自动领豆日志"  # 主题
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except Exception as e:
        print("发送失败")
    finally:
        s.quit()


if __name__ == '__main__':
    send()

