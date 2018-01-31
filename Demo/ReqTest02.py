import requests

response = requests.get("http://www.baidu.com")
if response.status_code == requests.codes.ok:
    print("访问成功")