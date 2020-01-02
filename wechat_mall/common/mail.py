import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

def mail():
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    # 邮件正文内容
    message.attach(MIMEText('微信商城自动化测试……', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    basedir = os.path.dirname(__file__)
    upload_path = os.path.join(basedir,"../report/result.html")
    att1 = MIMEText(open(upload_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="result.html"'
    message.attach(att1)

    mail = smtplib.SMTP()
    mail.connect("smtp.qq.com")  # 连接 qq 邮箱
    mail.login("1562662129@qq.com", "jyooapzxqisubagb")  # 账号和授权码
    mail.sendmail("1562662129@qq.com", ["1562662129@qq.com"], message.as_string())  # 发送账号、接收账号和邮件信息

if __name__ == '__main__':
    mail()
