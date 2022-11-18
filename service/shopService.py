from DAO.shopDAO import shopDAO



class shopService:
    def __init__(self) -> None:
        self.DAO=shopDAO()

    def login(self,shopId,password,shoptype,shopName,avePrice,address,phone,foods):
        return self.DAO.insert(shopId,password,shoptype,shopName,avePrice,address,phone,foods)

    def deleteShopByShopName(self,shopname):
        return self.DAO.deleteShopByShopname(shopname)

    def selectAllShop(self):
        return self.DAO.selectALL()
    def updateShop(self,username,st,si,pw,ap,add,phone,foods,sn):
        return self.DAO.update(username,st,si,pw,ap,add,phone,foods,sn)

    def deleteShop(self,id):
        if id!="":
            return self.DAO.delete(id)
        else:
            return False



    def selectShopByID(self,id):
        return self.DAO.selectShopByID(id)

    def selectByShopName(self,dest):
        return self.DAO.selectByname(dest)

    def nameMappingInGra(self,s,G):
        if s is None :
            return None

        # def __init__(self, totalDis, pre, dis) -> None:
        #     self.totalDis = totalDis  # 总距离
        #     self.pre = pre  # 前一个点的距离
        #     self.dis = dis  # 和前一个点的距离
        #     self.isVisite = False  # 默认没有被访问
        try:
            min=str(G.S[s.shopId].totalDis)
        except:
            min=1000000000
        return  min

    def recommend(self,shoptype,foodsname,com):
       return self.DAO.fuzzySearch(shoptype,foodsname,com)






