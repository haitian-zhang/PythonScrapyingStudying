# 思博特爬虫（从Excel读取）
import requests
from bs4 import BeautifulSoup
import xlrd

import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='python')
cur = conn.cursor()

data = xlrd.open_workbook('2015级本科新生名单.xls')
table = data.sheet_by_name(u'2015级本科新生名单')
nrows = table.nrows
students = table.col_values(7)
students.pop(0)

for student in students:
    try:
        params = {'operType': '911', 'loginflag': '0', 'loginType': '0', 'userName': student, 'passwd': student}
        r = requests.post("http://210.42.72.169/servlet/adminservlet", data=params)
        cookies = r.cookies
        r = requests.get("http://210.42.72.169/student/studentInfo.jsp?userName=" + student + "&passwd=" + student,
                         cookies=cookies)
        # 基本信息页面
        bsObj = BeautifulSoup(r.text, "lxml")
        table = bsObj.find('table', {'width': '100%', 'border': '0', 'cellpadding': '0', 'cellspacing': '1',
                                     'bgcolor': '#cdddf4', 'class': 's9'})
        trs = table.findAll("tr")
        studentNumber = str(trs[1].td.next_sibling.next_sibling.get_text().strip())
        name = str(trs[2].td.next_sibling.next_sibling.get_text().strip())
        sex = str(trs[3].td.next_sibling.next_sibling.get_text().strip())
        IDCardNumber = str(trs[4].td.next_sibling.next_sibling.get_text().strip())
        Nation = str(trs[5].td.next_sibling.next_sibling.get_text().strip())
        grade = str(trs[6].td.next_sibling.next_sibling.get_text().strip())
        class_ = str(trs[7].td.next_sibling.next_sibling.get_text().strip())
        # 身高体重页面
        r = requests.get(
            "http://210.42.72.169/SportWeb/health_info/listdetalhistroyScore.jsp?studentNo=" + student + "&academicYear=1718&gradeNo=" + str(
                int(grade[0]) - 1), cookies=cookies)
        bsObj2 = BeautifulSoup(r.text, "lxml")
        table2 = bsObj2.find('table', {'width': '100%', 'border': '0', 'cellpadding': '0', 'cellspacing': '1',
                                       'bgcolor': '#cdddf4', 'class': 's9'})
        trs2 = table2.findAll("tr")
        height = str(trs2[3].td.next_sibling.next_sibling.next_sibling.next_sibling.get_text().strip())
        weight = str(trs2[4].td.next_sibling.next_sibling.next_sibling.next_sibling.get_text().strip())

        sql = "insert into students values ('" + studentNumber + "','" + name + "', '" + sex + "', '" + IDCardNumber + "', '" + Nation + "', '" + grade + "', '" + class_ + "', '" + height + "', '" + weight + "')"
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
