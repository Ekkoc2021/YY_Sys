from service.shopService import shopService
from service.shopUserService import shopUserService


class shopController:
    def __init__(self) -> None:
        self.Service=shopService()
        self.shopuserService=shopUserService()

    # 注册
    def register(self):
        shopId = input("注册信息均不能为空\n账号(shopid):")
        password = input("密码:")
        # def __init__(self, shoptype,
        # shopId, shopName, avgScore,
        # avePrice, address, phone, foods, Comments)
        # 包括类型、ID、商家名称、密码、人均消费、地址、电话、特色菜
        shoptype = input("商店类型:")
        shopName = input("商店名称:")
        avePrice = input("人均消费:")
        address = input("地址:")
        phone = input("电话:")
        foods = input("特色食物:")
        if shopId != "" and password != "" and shoptype!="" and shopName!="" and avePrice!="" and address!=""\
                and phone!="" and foods!="":
           return self.Service.login(shopId,password,shoptype,shopName,avePrice,address,phone,foods)
        else:
            return False

    def showALLshopuser(self):
        shopList=self.Service.selectAllShop()
        for i in shopList:
            print(i)
        if len(shopList)==0:
            print("没有任何商家注册!")

    def selectShopName(self):
        shopname=input("商店名称:")
        shop=self.Service.selectByShopName(shopname)
        if shop is not None:
            print(shop)
        else:
            print("没有此商家!")
    def deleteShopByshopname(self):
        shopname=input("输入要删除的商店名称:")
        if self.Service.deleteShopByShopName(shopname):
            print("删除成功!")
        else:
            print("删除失败!可能是数据库连接失败,或者是数据库中无此商家,请重试。")
    def shopUserManage(self):
        while True:
            uc2 = input("-------------------\n1,所有商家\n2,查询商家\n3,删除商家\n4,返回\n-------------------\n")
            if uc2 == "1":
                self.showALLshopuser()
            elif uc2 == "2":
                self.selectShopName()
                pass
            elif uc2 == "3":
                self.deleteShopByshopname()
                pass
            elif uc2 == "4":
                break



    def showShopInf(self,shopUser):
        shops=self.Service.selectShopByID(shopUser.username)
        if len(shops)>0:
            for shop in shops:
                print("--------------\n你注册的餐馆信息如下:\n"+shop.__str__())
        else:
            print("你还没有创建餐馆!")

    def updateMyShop(self,shopUser):
        # def __init__(self, shoptype, shopId, shopName, avgScore, avePrice, address, phone, foods, Comments)
        # 包括类型、ID、商家名称、密码、人均消费、地址、电话、特色菜
        st=input("商店类型:")
        si=input("商店id:")
        sn=input("商店名称:")
        pw=input("密码:")
        ap=input("人均消费:")
        add=input("地址:")
        phone=input("电话:")
        foods=input("特色食物:")
        if self.Service.updateShop(shopUser.username,st,si,pw,ap,add,phone,foods,sn):
            print("更新成功!请重新登录!")
            return True
        else:
            print("更新失败!")
            return False
    def shutdownShop(self,shopUser):
        if self.Service.deleteShop(shopUser.username):
            print("删除成功!")
        else:
            print("删除失败!请重试!")

    #返回T表示要重新登录
    def manageShopInfor(self,shopUser):
        while True:
            c=input("-------------------\n商户:"+shopUser.username+
                    "\n1,查看餐馆信息\n2,修改餐馆信息\n3,注销餐馆\n4,退出\n")
            if c=="1":
                self.showShopInf(shopUser)
            elif c=="2":
                shops = self.Service.selectShopByID(shopUser.username)
                if len(shops)>0:
                    isUpdate=self.updateMyShop(shopUser)
                    if isUpdate:
                        return True
                else:
                    print("你还没有任何商店!")
            elif c=="3":
                self.shutdownShop(shopUser)
                return True
            elif c=="4":
                return True


    def recommend(self):
        shoptype=input("你喜欢的餐厅类别:")
        foodsname=input("你感兴趣特色菜:")
        com=input("你喜欢的餐厅特点:")
        shoplist=self.Service.recommend(shoptype,foodsname,com)
        if len(shoplist)>0:
            for i in shoplist:
                print(i)
        else:
            print("没有匹配餐厅!")

    def GMapping(self,G,ok):
        destination = input("输入目的餐厅称:")
        s=self.Service.selectByShopName(destination)
        if s is not None:
            print("-------------------\n餐厅基本信息\n"+s.__str__())
            if ok :
                min = self.Service.nameMappingInGra(s,G)
                if min is not None:
                    print("你从矿大到" + destination + "最短距离是:" + str(min)+"km")
                else:
                    print("这个店可能地址存在异常!无法计算距离!")
            else:
                print("计算最短距离中....可以先体验其他功能,稍后再来!")
        else:
            print("这个餐厅还没有加入到我们的系统!")
