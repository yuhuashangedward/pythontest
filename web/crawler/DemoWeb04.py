import  requests

# 请求豆瓣读书网点

r = requests.get('https://book.douban.com')
print(r.status_code)

print(r.headers['content-type'])

print(r.encoding)
print(r.text)
print(r.cookies)
print(r.headers)
print(r.url)



