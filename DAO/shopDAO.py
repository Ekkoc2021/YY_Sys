from pymysql import MySQLError

from DAO.databaseUtil import getC
from table import shop


class shopDAO:
    def __init__(self) -> None:
        super().__init__()

    def insert(self,shopId,password,shoptype,shopName,avePrice,address,phone,foods):
        sql = "insert into shop(shopId,shoptype,shopName,avePrice,address,phone,foods) value(%s,%s,%s,"+avePrice+",%s,%s,%s)"
        sql2 = "insert into shopuser value (%s,%s)"
        conn = getC()
        isInsert = False
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, [shopId,shoptype,shopName,address,phone,foods])
            with conn.cursor() as cursor:
                cursor.execute(sql2, [shopId,password])
            conn.commit()
            isInsert = True
        except MySQLError:
            # 手动回滚
            conn.rollback()
        # 第五步：关闭连接
        finally:
            conn.close()
            return isInsert

    def deleteShopByShopname(self,shopname):
        shop=self.selectByname(shopname)
        if shop is None:
            return False
        else:
            return self.delete(shop.shopId)

    def delete(self,id):
        sql="delete from shop where shopId=%s"
        sql2="delete from shopuser where username=%s"
        conn = getC()
        isDelete=False
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql,[id])
            with conn.cursor() as cursor:
                cursor.execute(sql2,[id])
            conn.commit()
            isDelete = True
        except MySQLError:
            # 手动回滚
            conn.rollback()
        # 第五步：关闭连接
        finally:
            conn.close()
            return isDelete

    def update(self,username,st,pi,pw,ap,add,phone,foods,sn):
        #  shoptype, shopId, shopName, avgScore, avePrice,
        #  address, phone, foods, Comments
        isUpdate=False
        sql="update shop set "
        sql2="update shopuser set "
        isJion=False
        isJion2=False
        # shoptype shopId  shopName avgScore
        # avePrice
        # address
        # phone
        # foods
        # Comments
        if st!="":
            sql+="shoptype='"+st+"'"
            isJion=True
        if pi!="":
            if isJion:
                sql+=" , shopId='"+pi+"'"
            else:
                sql+=" shopId='"+pi+"'"
                isJion=True
            sql2+=" username='"+pi+"'"
            isJion2=True
        if pw !="":
            if isJion2:
                sql2 += ",password='" + pw + "'"
            else:
                sql2 += " password='" + pw + "'"
        if ap!="":
            if isJion:
                sql += " , avePrice='" + ap + "'"
            else:
                sql += "  avePrice='" + ap + "'"
                isJion=True
        if add!="":
            if isJion:
                sql += " , address='" + add + "'"
            else:
                sql += " address='" + add + "'"
                isJion=True
        if phone!="":
            if isJion:
                sql += " , phone='" + phone + "'"
            else:
                sql += " phone='" + phone + "'"
                isJion=True
        if sn!="":
            if isJion:
                sql += ",shopname='" + sn + "'"
            else:
                sql += " shopname='" + sn + "'"

        if foods!="":
            if isJion:
                sql += ",foods='" + foods + "'"
            else:
                sql += " foods='" + foods + "'"

        sql=sql+"  where shopId='"+username+"'"
        sql2=sql2+"  where username='"+username+"'"
        conn = getC()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql)
            with conn.cursor() as cursor:
                cursor.execute(sql2)

            conn.commit()
            isUpdate=True
        except MySQLError:
            # 手动回滚
            conn.rollback()
        # 第五步：关闭连接
        finally:
            conn.close()
            return isUpdate

    def selectALL(self):
        sql = "select * from shop;"
        conn = getC()
        shops = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    shoptype = row[0]
                    id = row[1]
                    name = row[2]
                    aveScore = row[3]
                    avePrice = row[4]
                    address = row[5]
                    phone = row[6]
                    foods = row[7]
                    comm = row[8]
                    shops.append(shop(shoptype, id, name, aveScore, avePrice, address, phone, foods, comm))
        except MySQLError:
            print("查询失败!数据库或已关闭!")
        # 第五步：关闭连接
        finally:
            conn.close()
            return shops

    def selectShopByID(self,id):
        sql = "select * from shop where shopId=%s;"
        conn = getC()
        shops = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, [id])
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    shoptype = row[0]
                    id = row[1]
                    name = row[2]
                    aveScore = row[3]
                    avePrice = row[4]
                    address = row[5]
                    phone = row[6]
                    foods = row[7]
                    comm = row[8]
                    # 打印结果
                    # def __init__(self, shoptype, shopId, shopName, avgScore, avePrice, address, phone, foods, Comments)
                    # shop : shoptype,shopId,shopName,avgScore,avePrice,address,phone,foods,Comments
                    shops.append(shop(shoptype, id, name, aveScore, avePrice, address, phone, foods, comm))
        except MySQLError:
            print("查询失败!数据库或已关闭!")
        # 第五步：关闭连接
        finally:
            conn.close()
            return shops

    #处理推荐
    def fuzzySearch(self,shoptype,foodsname,com):

        sql1 = "select * from shop"
        joinTime=0
        if  shoptype !="" or foodsname!="" or com!="" :
            sql1=sql1+" where "
            if shoptype is not None and shoptype !="":
                sql1=sql1+"shoptype like '%"+shoptype+"%' "
                joinTime+=1
            if foodsname is not None and foodsname !="":
                if joinTime==0:
                    sql1=sql1+"foods like \'%"+foodsname+"%\' "
                    joinTime+=1
                else:
                    sql1 = sql1 + "and foods like \'%"+foodsname+"%\' "
            if com is not None and com !="":
                sql1=sql1+"Comments like '%"+com+"%\'"

            sql1+="  order by avgScore desc;"
        conn = getC()
        shoplist = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql1)
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    shoptype = row[0]
                    id = row[1]
                    name = row[2]
                    aveScore = row[3]
                    avePrice = row[4]
                    address = row[5]
                    phone = row[6]
                    foods = row[7]
                    comm = row[8]
                    # 打印结果
                    # def __init__(self, shoptype, shopId, shopName, avgScore, avePrice, address, phone, foods, Comments)
                    # shop : shoptype,shopId,shopName,avgScore,avePrice,address,phone,foods,Comments
                    shoplist.append(shop(shoptype, id, name, aveScore, avePrice, address, phone, foods, comm))
        except MySQLError:
            # 手动回滚
            conn.rollback()
        # 第五步：关闭连接
        finally:
            conn.close()
            return shoplist


    def selectByname(self, dest):
        sql = "select * from shop where shopName=%s;"
        conn = getC()
        s=None
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql,[dest])
                results = cursor.fetchall()
                for row in results:  # 遍历查询结果
                    shoptype = row[0]
                    id = row[1]
                    name = row[2]
                    aveScore = row[3]
                    avePrice = row[4]
                    address=row[5]
                    phone=row[6]
                    foods=row[7]
                    comm=row[8]
                    # 打印结果
                    # def __init__(self, shoptype, shopId, shopName, avgScore, avePrice, address, phone, foods, Comments)
                    #shop : shoptype,shopId,shopName,avgScore,avePrice,address,phone,foods,Comments
                    s=shop(shoptype,id,name,aveScore,avePrice,address ,phone,foods,comm)
        except MySQLError:
            # 手动回滚
            conn.rollback()
        # 第五步：关闭连接
        finally:
            conn.close()
            return s
