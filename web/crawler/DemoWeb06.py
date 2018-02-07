import  requests

resp = requests.get('http://www.baidu.com')
print(resp.status_code)
print(resp.encoding)
print(resp.text)
resp.encoding = "UTF-8"
print(resp.text)