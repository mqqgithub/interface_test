'''
1、不启用fiddler，直接发https请求，不会有SSL问题（也就是说不想看到SSL问题，关掉fiddler就行）
2、Requests的请求默认verify=True、如果你将 verify设置为 False，Requests 也能忽略对 SSL 证书的验证
'''
import urllib3
import requests
# 禁用安全请求警告
urllib3.disable_warnings()
url = "https://passport.cnblogs.com/user/signin"
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
          }
r = requests.get(url, headers=headers, verify=False)
print(r.status_code)
