import smtplib
from email.header import Header  # 用来设置邮件头和邮件主题
from email.mime.text import MIMEText  # 发送正文只包含简单文本的邮件，引入MIMEText即可
class email():
    def sendemail(self):
        # 发件人和收件人
        sender = 'mqq508@163.com'
        receiver = '767738633@qq.com'

        # 所使用的用来发送邮件的SMTP服务器
        smtpServer = 'smtp.163.com'

        # 发送邮箱的用户名和授权码（不是登录邮箱的密码）
        username = 'mqq508@163.com'
        password = 'mqq123'

        mail_title = '自动化测试报告'
        mail_body = '这里是邮件的正文'

        # 创建一个实例   https://www.cnblogs.com/zhangxinqi/p/9113859.html
        message = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文
        message['From'] = sender  # 邮件上显示的发件人
        message['To'] = receiver  # 邮件上显示的收件人
        message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

        try:
            smtp = smtplib.SMTP()  # 创建一个连接
            smtp.connect(smtpServer)  # 连接发送邮件的服务器
            smtp.login(username, password)  # 登录服务器
            smtp.sendmail(sender, receiver, message.as_string())  # 填入邮件的相关信息并发送
            print("邮件发送成功！！！")
            smtp.quit()
        except smtplib.SMTPException:
            print("邮件发送失败！！！")


if __name__=='__main__':
    e = email()
    e.sendemail()