from datetime import datetime
now = datetime.now() #初始化datetime类的时间
timestamp = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
print(timestamp)