# 我的网站
# 查看页面
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://pythonscraping.com/pages/files/form.html")
# bsObj = BeautifulSoup(html.read(), "html.parser")
# print(bsObj)


# 提交表单
import requests
params = {'username': '王少刚', 'password': 'wsg727', 'method': 'login', 'submit': '登录'}
r = requests.post("http://120.79.60.89/user", data=params)
print(r.text)