from pymysql import MySQLError

from DAO.databaseUtil import getC
from table import order


class orderDao:
    def __init__(self) -> None:
        super().__init__()

    def selectShopOrderWithLimit(self,shopid, limit):
        sql = "select order1.account,order1.shopname,order1.ordertime from shopuser,order1,shop where shopuser.username=%s and shopuser.username=shop.shopId and shop.shopname=order1.shopname limit "+str(limit)
        conn = getC()
        orderList = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, [shopid])
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    a = row[0]
                    sn = row[1]
                    t = row[2]
                    orderList.append(order(a, sn, t))
        except MySQLError:
            print()
        finally:
            conn.close()
            return orderList

    def selectOrderByShopnameAndUsername(self, shopname, account):
        sql="select * from order1 where shopname=%s and account=%s order by ordertime"
        conn = getC()
        orderList = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, [shopname,account])
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    a = row[0]
                    sn = row[1]
                    t = row[2]
                    orderList.append(order(a, sn, t))

        except MySQLError:
            print()
        finally:
            conn.close()
            return orderList

    def selectOrderByAccount(self, account):
        sql = "select * from order1 where account=%s order by ordertime;"
        conn = getC()
        orderList = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, [account])
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    a = row[0]
                    sn = row[1]
                    t = row[2]
                    orderList.append(order(a, sn, t))

        except MySQLError:
            print()
        finally:
            conn.close()
            return orderList

    def selectOrderByShopName(self,shopname):
        sql = "select * from order1 where shopname=%s order by ordertime;"
        conn = getC()
        orderList = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, [shopname])
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    a = row[0]
                    sn = row[1]
                    t = row[2]
                    orderList.append(order(a, sn, t))

        except MySQLError:
            print()
        finally:
            conn.close()
            return orderList

    def insert(self,order):
        sql = "insert into order1 value(%s,%s,%s);"
        conn = getC()
        orderList = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, [order.account,order.shopname,order.ordertime])
            conn.commit()
        except MySQLError:
            return False
        finally:
            conn.close()
            return True

    def delete(self,order):
        isDelete=False
        if order is not None:
            sql = "delete from order1 where account=%s and shopname=%s and ordertime=%s"
        conn = getC()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, [order.account,order.shopname,order.ordertime])
            conn.commit()
            isDelete=True
        except MySQLError:
            # 手动回滚
            conn.rollback()
            print("删除失败!")
            isDelete=False
        # 第五步：关闭连接
        finally:
            conn.close()
            return isDelete
