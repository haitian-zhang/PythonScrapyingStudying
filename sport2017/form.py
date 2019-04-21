# 学习
# 查看页面
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://pythonscraping.com/pages/files/form.html")
# bsObj = BeautifulSoup(html.read(), "html.parser")
# print(bsObj)


# 提交表单
import requests
params = {'firstname': 'shaogang', 'lastname': 'wang'}
r = requests.post("http://pythonscraping.com/pages/files/processing.php", data=params)
print(r)