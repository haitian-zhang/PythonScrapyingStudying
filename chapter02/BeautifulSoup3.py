# 查找后代标签

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
imgs = bsObj.find("table", {"id": "giftList"}).tr.next_siblings
for child in imgs:
    try:
        A = child.findAll("img")
        for a in A:
            print(a)
    except:
        pass
    # print(type(child))

