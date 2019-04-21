# 处理cookie
# 查看页面
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://pythonscraping.com/pages/files/form.html")
# bsObj = BeautifulSoup(html.read(), "html.parser")
# print(bsObj)


# 提交表单
import requests
params = {'username': '911', 'password': 'password'}
r = requests.post("http://www.pythonscraping.com/pages/cookies/welcome.php", data=params)
print("Cookie is set to: " + str(r.cookies.get_dict()))
print("------------")
r = requests.post("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)