import urllib.request
import json

op = urllib.request.urlopen("http://httpbin.org/json")
data = op.read().decode('utf-8')
print(data)

obj = json.loads(data)
print(obj)