# 使用MySQL
import pymysql
# 创建连接对象conn
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='python')
# 创建光标对象cur
cur = conn.cursor()
sql = "SELECT URI FROM baike LIMIT 5"
# 执行sql语句
cur.execute(sql)
# 获取结果集
rs = cur.fetchall()
i = 0
for (r,) in rs:
    print(r)
# 关闭光标对象
cur.close()
# 关闭连接对象
conn.close()
