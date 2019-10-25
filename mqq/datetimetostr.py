from datetime import datetime
import random

#把当前的时间戳生成数字字符串
now = datetime.now() #初始化datetime类的时间
strnow = datetime.strftime(now,'%Y%m%d%H%M%S')+"".join(random.choice("0123456789") for i in range(9))
print(strnow)
#随机产生手机号
s = random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
print(s)