from pymysql import MySQLError

from DAO.databaseUtil import getC
from table import user


class userDAO:
    def __init__(self) -> None:
        # create table
        #         # user(account
        #         # varchar(32), password
        #         # varchar(32), contact
        #         # varchar(32));
        super().__init__()

    def selectAll(self):
        sql = "select * from user"
        conn = getC()
        userList=[]
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    n = row[0]
                    p = row[1]
                    c = row[2]
                    # 打印结果
                    u3 = user(n, p, c)
                    userList.append(u3)
        except MySQLError:
            conn.close()
            return userList

        conn.close()
        return userList

    def select(self, u):
        sql = "select * from user where account=%s and password=%s"
        conn = getC()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql,[u.account,u.password])
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    n = row[0]
                    p = row[1]
                    c=row[2]
                    # 打印结果
                    u3=user(n, p, c)
                    conn.close()
                    return u3
        except MySQLError:
            conn.close()
            return user()

        conn.close()
        return user()

    def insert(self,su):
        if su.contact is not None:
            sql="insert into user value (%s,%s,%s);"
            conn = getC()
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql, [su.account, su.password,su.contact])
                conn.commit()
            except MySQLError:
                conn.rollback()
                conn.close()
                return False
                # 手动回滚
        else:
            sql = "insert into user(account,password)  value (%s,%s);"
            conn = getC()
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql, [su.account, su.password])
                conn.commit()
            except MySQLError:
                conn.rollback()
                conn.close()
                return False
                # 手动回滚
        conn.close()
        return True

    def selectUserByAccount(self,Account):
        sql="select * from user where account=%s"
        # conn = pymysql.connect(
        #     host="localhost",
        #     database="YYOrderSystem",
        #     user="root",
        #     password="qwe456654.",
        #     port=3306
        # )
        conn=getC()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql,[Account])
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    a = row[0]
                    p = row[1]
                    c = row[2]
                    # 打印结果
                    return user(a,p,c)
            conn.commit()
        except MySQLError:
            # 手动回滚
            conn.rollback()
        # 第五步：关闭连接
        finally:
            conn.close()

    def updateUserPassword(self,account,password):
        if account is not None and password is not None:
            sql=" update user set password=%s where account=%s"
        conn=getC()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql,[password,account])
            conn.commit()
        except MySQLError:
            # 手动回滚
            conn.rollback()
            print("修改失败!")
        # 第五步：关闭连接
        finally:
            conn.close()

    def updateUserContact(self,account,contact):
        if account is not None and contact is not None:
            sql = " update user set contact=%s where account=%s"
        conn=getC()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql,[contact,account])
            conn.commit()
        except MySQLError:
            # 手动回滚
            conn.rollback()
            print("修改失败!")
        # 第五步：关闭连接
        finally:
            conn.close()

    def deleteUser(self,account):
        isDelete=False
        if account is not None:
            sql="delete from user where account=%s"
        conn=getC()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql,[account])
            conn.commit()
            isDelete=True
        except MySQLError:
            # 手动回滚
            conn.rollback()
        # 第五步：关闭连接
        finally:
            conn.close()
            return isDelete