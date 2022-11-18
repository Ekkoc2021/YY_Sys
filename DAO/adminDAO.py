from pymysql import MySQLError

from DAO.databaseUtil import getC
from table import admin


class adminDAO:
    def select(self, ad):
        sql = "select * from admin where username=%s and password=%s"
        # conn = pymysql.connect(
        #     host="localhost",
        #     database="YYOrderSystem",
        #     user="root",
        #     password="qwe456654.",
        #     port=3306
        # )
        conn = getC()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, [ad.username, ad.password])
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    n = row[0]
                    p = row[1]
                    # 打印结果
                    return admin(n, p)
        except MySQLError:
            conn.close()
            return admin()
        conn.close()
        return admin()