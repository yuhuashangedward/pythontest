import requests

files = {"files":open("git.jpg", "rb")}
response = requests.post("http://httpbin.org/post",files=files)
print(response.text)