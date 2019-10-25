from suds.client import Client
url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = Client(url)
print(client)

res = client.service.getMobileCodeInfo(13888888888)
print(res)