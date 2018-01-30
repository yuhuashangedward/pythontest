#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-
import requests
response = requests.get("https://www.baidu.com/", verify=True)

# 也可以省略不写
# response = requests.get("https://www.baidu.com/")
# 如果SSL证书验证不通过，或者不信任服务器的安全证书，则会报出SSLError
print(response.text)


