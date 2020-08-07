import json
str1 = '{ "params":{"id":222,"offset":0}, "nodename":"topic" }'
params = json.loads(str1)
print(params)
print(type(params))