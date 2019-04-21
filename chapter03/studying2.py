# 豆瓣爬虫
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 整合mysql
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='python')
cur = conn.cursor()
cur.execute("USE python")

def getLinks(pageUrl="https://book.douban.com", pages = []):
    try:
        html = urlopen(pageUrl)
        bsObj = BeautifulSoup(html, "html.parser")
        for link in bsObj.findAll("a", href=re.compile("^(https://book.douban.com/subject/)[0-9]*[/]$")):
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                name = link.parent.next_sibling.next_sibling.get_text().strip()
                pages.append(newPage)
                print(newPage, name)
                # 插入数据库
                sql = "INSERT INTO books (URI, name) VALUES ('" + newPage + "','" + name + "')"
                try:
                    cur.execute(sql)
                    conn.commit()
                except:
                    # 重复不提交
                    print("重复")
                getLinks(pageUrl=newPage, pages=pages)
    except:
        print("禁止访问，10秒后重试。。。")
        time.sleep(10)
        getLinks(pageUrl=pageUrl, pages=pages)

getLinks()
cur.close()
conn.close()
print("运行结束")