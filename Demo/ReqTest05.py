import requests

result = requests.get('http://www.pythontab.com')


print(result.status_code)
print(result.headers['content-type'])
print(result.encoding)
print(result.content)