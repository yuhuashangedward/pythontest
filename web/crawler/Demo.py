import requests

response = requests.get("https://www.alibaba.com")
print(type(response))
print(response.status_code)
print(type(response.text))

response.encoding = "utf-8"
#print(response.text)

print(response.cookies)

print(response.content)
print(response.content.decode("utf-8"))