# 百度百科爬虫
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import sys
sys.setrecursionlimit(100000)

# 整合mysql
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='python')
cur = conn.cursor()
cur.execute("USE python")

def getLinks(pageUrl="https://baike.baidu.com/item/Java", pages = []):
    try:
        html = urlopen(pageUrl)
        bsObj = BeautifulSoup(html, "html.parser")
        for link in bsObj.findAll("a", href=re.compile("^(/item/)")):
            if "https://baike.baidu.com" + link.attrs['href'] not in pages:
                # 获取词条名称同时去掉两边的空格
                name = link.get_text().strip()
                newPage = "https://baike.baidu.com" + link.attrs['href']
                pages.append(newPage)
                # 检测是否在数据库中存在
                sql0 = "SELECT * FROM baike WHERE URI='" + newPage + "'"
                cur.execute(sql0)
                if cur.fetchone() == None:
                    # 插入数据库
                    sql = "INSERT INTO baike (URI, name) VALUES ('" + newPage + "','" + name + "')"
                    try:
                        cur.execute(sql)
                        conn.commit()
                        print(newPage, name)
                    except:
                        # 异常处理
                        print("插入失败")
                    getLinks(pageUrl=newPage, pages=pages)

    except:
        print("禁止访问，10秒后重试。。。")
        time.sleep(10)
        getLinks(pageUrl=pageUrl, pages=pages)
getLinks()
# cur.close()
# conn.close()
print("运行结束")