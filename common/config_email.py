import smtplib
import os
from email.header import Header  # 用来设置邮件头和邮件主题
from email.mime.text import MIMEText  # 发送正文只包含简单文本的邮件，引入MIMEText即可
from email.mime.application import MIMEApplication # 发送各种附件
from email.mime.multipart import MIMEMultipart
from common.getpathInfo import get_base_path


class Email(object):

    def send_email(self):
        # 发件人和收件人
        sender = 'mqq508@163.com'
        receiver = '756738633@qq.com'

        # 所使用的用来发送邮件的SMTP服务器
        smtpServer = 'smtp.163.com'

        # 发送邮箱的用户名和授权码（不是登录邮箱的密码）
        username = 'mqq508@163.com'
        password = 'mqq123'

        mail_title = '自动化测试报告'
        # mail_body = '这里是邮件的正文'

        # 创建一个实例
        # msg = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文

        msg = MIMEMultipart()
        msg['From'] = sender  # 邮件上显示的发件人
        msg['To'] = receiver  # 邮件上显示的收件人
        msg['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

        # ---这是文字部分---
        part = MIMEText("接口自动化测试报告")
        msg.attach(part)

        # ---这是附件部分---
        attach_path = os.path.join(get_base_path(), 'result', 'report.html')
        part = MIMEApplication(open(attach_path, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename="report.html")
        msg.attach(part)
        '''
        # xlsx类型附件
        part = MIMEApplication(open('foo.xlsx', 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename="foo.xlsx")
        msg.attach(part)

        # jpg类型附件
        part = MIMEApplication(open('foo.jpg', 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename="foo.jpg")
        msg.attach(part)

        # pdf类型附件
        part = MIMEApplication(open('foo.pdf', 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
        msg.attach(part)

        # mp3类型附件
        part = MIMEApplication(open('foo.mp3', 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename="foo.mp3")
        msg.attach(part)
        '''

        try:
            smtp = smtplib.SMTP()  # 创建一个连接
            smtp.connect(smtpServer)  # 连接发送邮件的服务器
            smtp.login(username, password)  # 登录服务器
            smtp.sendmail(sender, receiver, msg.as_string())  # 填入邮件的相关信息并发送
            print("邮件发送成功！！！")
            smtp.quit()
        except smtplib.SMTPException:
            print("邮件发送失败！！！")


if __name__ == '__main__':
    e = Email()
    e.send_email()
    
    
