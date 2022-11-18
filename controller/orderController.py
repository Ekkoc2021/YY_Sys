from service.orderService import orderService
from service.shopService import shopService
from table import order


class orderController:
    def __init__(self) -> None:
        self.Service=orderService()
        self.shopService01=shopService()

    def userOrderByName(self,shopname):
        self.Service.OrderByShopName(shopname)

    def addOrder(self,order):
        sp=self.shopService01.selectByShopName(order.shopname)
        if sp is not None:
            if self.Service.add(order):
                print("订单添加成功!")
            else:
                print("订单添加失败!")
        else:
            print("餐厅不存在")

    #返回是否删除成功
    def cancelOrder(self,order):
        return self.Service.deleteOrder(order)

    def manageOrder(self,user):
        orderList=None
        while True:
            c=input("用户名:"+user.account+"\n当前位置预定处理\n1,所有预定\n2,根据餐馆筛选预定\n3,添加预定\n4,取消预定\n5,返回\n-------------------\n")
            if c=="1":
                orderList = self.Service.suserOrders(user.account)
                for i in range(len(orderList)):
                    print(str(i + 1) + "," + orderList[i].__str__())
                if len(orderList)==0:
                    print("没有预定!")
            elif c=="2":
                orderList = self.Service.suserOrders(user.account)
                sn=input("商店名称:")
                j=0
                for i in range(len(orderList)):
                    if orderList[i].shopname==sn:
                        print(str(j + 1) + "," + orderList[i].__str__())
                        j+=1
                print()
            elif c=="3":
                sn=input("商店名称:")
                ot=input("订单时间:")
                ord=order(user.account,sn,ot)
                self.addOrder(ord)
            elif c=="4":
                orderList = self.Service.suserOrders(user.account)
                for i in range(len(orderList)):
                    print(str(i + 1) + "," + orderList[i].__str__())
                while 0==0:
                    try:
                        uc=eval(input("-------------------\n用户名:"+user.account+"\n当前位置取消预定"+"选择要取消(输入号,输入0退出):"))
                        if uc==0:
                            break
                        elif uc>len(orderList):
                            1/0
                        elif self.cancelOrder(orderList[uc-1]):
                            print("删除成功!")
                        else:
                            print("删除失败!")
                    except:
                        print("无效指令!重新输入")
                print()
            elif c=="5":
                print("退出预定处理功能!")
                break

    def dealWithShopOrder(self,shopUser):
        #todo ing
        limit=input("删除最早前n订单\n输入删除的数量n:")
        orderList = self.Service.selectShopOrderWithLimit(shopUser.username,limit)
        for i in orderList:
            print(i)
            self.cancelOrder(i)
        print("删除完成!")


    def showShopAllOrder(self,shopUser):
        orderList=self.Service.selectByShopName(shopUser.username)
        for i in orderList:
            print(i)
        if len(orderList) == 0:
            print("当前商店没有订单!")

    def selectShopOrderByUsername(self,shopUser):
        account=input("用户账号:")
        orderList=self.Service.selectOrderByShopnameAndUsername(shopUser.username,account)
        for i in orderList:
            print(i)
        if len(orderList)==0:
            print("没有该用户的订单信息!")
    def manageShopOrder(self,shopUser):
        while True:
            c=input("-------------------\n商户:"+shopUser.username+
                    "\n1,查询所有预定\n2,处理特定用户预定\n3,按照时间处理预定\n4,退出\n")
            if c=="1":
                self.showShopAllOrder(shopUser)
                pass
            elif c=="2":
                self. selectShopOrderByUsername(shopUser)
                pass
            elif c=="3":
                self.dealWithShopOrder(shopUser)
                pass
            elif c=="4":
                break