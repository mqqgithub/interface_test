# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
import urllib3
import hashlib
urllib3.disable_warnings()


# 作者：上海-悠悠 QQ交流群：512200893

class LoginLgw():

    def __init__(self, s):
        self.s = s

    def getTokenCode(self):
        '''
            要从登录页面提取token，code， 然后在头信息里面添加
            <!-- 页面样式 --><!-- 动态token，防御伪造请求，重复提交 -->
            <script type="text/javascript">
                window.X_Anti_Forge_Token = 'dde4db4a-888e-47ca-8277-0c6da6a8fc19';
                window.X_Anti_Forge_Code = '61142241';
            </script>
        '''
        url = 'https://passport.lagou.com/login/login.html'
        h = {
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            }
        # 更新session的headers
        self.s.headers.update(h)
        data = self.s.get(url, verify=False)
        soup = BeautifulSoup(data.content, "html.parser", from_encoding='utf-8')
        tokenCode = {}
        try:
            t = soup.find_all('script')[1].get_text()
            print(t)
            tokenCode['X_Anti_Forge_Token'] = re.findall(r"Token = '(.+?)'", t)[0]
            tokenCode['X_Anti_Forge_Code'] = re.findall(r"Code = '(.+?)'", t)[0]
            return tokenCode
        except:
            print("获取token和code失败")
            tokenCode['X_Anti_Forge_Token'] = ""
            tokenCode['X_Anti_Forge_Code'] = ""
            return tokenCode

    def encryptPwd(self,passwd):
        # 对密码进行了md5双重加密
        passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()
        # veennike 这个值是在js文件找到的一个写死的值
        passwd = 'veenike'+passwd+'veenike'
        passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()
        return passwd

    def login(self, user, psw):
        '''
        function:登录拉勾网网站
        :param user: 账号
        :param psw: 密码
        :return: 返回json
        '''
        gtoken = self.getTokenCode()
        print(gtoken)
        print(gtoken['X_Anti_Forge_Token'])
        print(gtoken['X_Anti_Forge_Code'])
        url2 = 'https://passport.lagou.com/login/login.json'
        h2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "X-Anit-Forge-Token": gtoken['X_Anti_Forge_Token'],
        "X-Anit-Forge-Code": gtoken['X_Anti_Forge_Code'],
        "Referer": "https://passport.lagou.com/login/login.html",
        }

        # 更新s的头部
        self.s.headers.update(h2)
        passwd = self.encryptPwd(psw)

        body = {
                "isValidate":'true',
                "username": user,
                "password": passwd,
                "request_form_verifyCode": "",
                "submit": ""
                }
        r2 = self.s.post(url2 , data=body, verify=False)
        try:
            print(r2.text)
            return r2.json()
        except:
            print("登录异常信息：%s" % r2.text)
            return None

if __name__ == "__main__":
    s = requests.session()
    lgw = LoginLgw(s)
    lgw.login("15221000000", "123456")