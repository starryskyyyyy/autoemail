import smtplib
import os
from email.mime.text import MIMEText

sender  = os.environ['EMAIL_SENDER']
password = os.environ['EMAIL_PASSWORD']

receiver = "starryskyyy@qq.com"

msg = MIMEText("早上好，这是测试的自动发送的邮件。")
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = "测试邮件"

with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())

print("邮件发送成功！")