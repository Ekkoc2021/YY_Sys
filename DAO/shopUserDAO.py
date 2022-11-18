from pymysql import MySQLError

from DAO.databaseUtil import getC
from table import shopUser


class shopUserDAO:
    def select(self, su):
        sql = "select * from shopUser where username=%s and password=%s"
        conn = getC()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, [su.username, su.password])
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    n = row[0]
                    p = row[1]
                    # 打印结果
                    return shopUser(n, p)
        except MySQLError:
            conn.close()
            return shopUser()
            # 手动回滚
        conn.close()
        return shopUser()

    def insert(self,su):
        sql="insert into shopUser value (%s,%s);"
        conn = getC()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, [su.username, su.password])

        except MySQLError:
            conn.rollback()
            conn.close()
            return False
            # 手动回滚
        conn.commit()
        conn.close()
        return True
