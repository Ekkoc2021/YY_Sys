from pymysql import MySQLError

from DAO.databaseUtil import getC
from table import distance

class edge:
    def __init__(self, shop1, shop2, distance) -> None:
        self.s1 = shop1
        self.s2 = shop2
        self.d = distance
class distanceDAO:
    def __init__(self) -> None:
        super().__init__()

    def selectIdByname(self, dest):
        sql = "select * from distince where shopName1=%s or shopName2=%s;"
        conn = getC()
        dis = None
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, [dest, dest])
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    i1 = row[0]
                    n1 = row[1]
                    i2 = row[2]
                    n2 = row[3]
                    dis = row[4]
                    # 打印结果
                    # def __init__(self, shoptype, shopId, shopName, avgScore, avePrice, address, phone, foods, Comments)
                    # shop : shoptype,shopId,shopName,avgScore,avePrice,address,phone,foods,Comments
                    dis = distance(i1, n1, i2, n2, dis)
        except MySQLError:
            # 手动回滚
            conn.rollback()
        # 第五步：关闭连接
        finally:
            conn.close()
            return dis

    def selectAlltoEdge(self):
        sql = "select * from distance;"
        conn = getC()
        edges = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    i1 = row[0]
                    n1 = row[1]
                    i2 = row[2]
                    n2 = row[3]
                    dis = row[4]
                    edges.append(edge(i1, i2, dis))
        except MySQLError:
            # 手动回滚
            print()
        # 第五步：关闭连接
        finally:
            conn.close()
            return edges
