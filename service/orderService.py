from DAO.orderDAO import orderDao
from DAO.shopDAO import shopDAO


class orderService:
    def __init__(self) -> None:
        self.DAO=orderDao()


    def selectShopOrderWithLimit(self,shopid,limit):
        return self.DAO.selectShopOrderWithLimit(shopid,limit)

    def selectOrderByShopnameAndUsername(self,shopid,account):
        s = shopDAO()
        shops = s.selectShopByID(shopid)
        if len(shops) > 0:
            return self.DAO.selectOrderByShopnameAndUsername(shops[0].shopName, account)
        else :
            return []

    def selectByShopName(self,username):
        s=shopDAO()
        shops=s.selectShopByID(username)
        if len(shops)>0:
            return self.DAO.selectOrderByShopName(shops[0].shopName)
        else:
            return []
    def suserOrders(self,account):
        return self.DAO.selectOrderByAccount(account)

    # 通过商店名称查找订单:返回一个列表
    def OrderByShopName(self, shopname):
        return self.DAO.selectOrderByShopName(shopname)

    def add(self,order):
        return self.DAO.insert(order)

    def deleteOrder(self,order):
        return self.DAO.delete(order)