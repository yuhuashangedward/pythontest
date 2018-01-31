import requests

from requests.auth import HTTPBasicAuth

response = requests.get("http://120.25.67.84:9001/",auth=HTTPBasicAuth("wangzhengwei","123456"))
print(response.status_code)