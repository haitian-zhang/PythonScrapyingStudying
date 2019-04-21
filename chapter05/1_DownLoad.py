# 文件下载
from urllib.request import urlopen, urlretrieve
import sys
sys.setrecursionlimit(100000)

# 整合mysql
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='python')
cur = conn.cursor()
cur.execute("USE python")

sql0 = "SELECT URI FROM baike LIMIT 5"
cur.execute(sql0)
rs = cur.fetchall()
# print(rs)
i = 0
for (r,) in rs:
    i = int(i) + 1
    name = r+'.html'
    # print(name)
    urlretrieve(r, filename='1_DownLoadFiles/' + str(i) + '.html')
cur.close()
conn.close()
print("运行结束")