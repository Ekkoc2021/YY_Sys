
class shopUser:

    def __init__(self,username=None,password=None) -> None:
        self.username=username
        self.password=password

class admin:

    def __init__(self,username=None,password=None) -> None:
        self.username = username
        self.password = password


class user:
    def __init__(self,account=None,password=None,contact=None) -> None:
        # create
        # table
        # user(account
        # varchar(32), password
        # varchar(32), contact
        # varchar(32));
        self.account=account
        self.password=password
        self.contact=contact

    def __str__(self) -> str:
        return "账号:"+str(self.account)+"  密码:"+str(self.password)+"  联系方式:"+str(self.contact)


class shop:
    def __init__(self,shoptype,shopId,shopName,avgScore,avePrice,address,phone,foods,Comments) -> None:
        # create  table shop
        # (shoptype varchar(32),
        self.shoptype=shoptype
        # shopId
        self.shopId=shopId
        # varchar(32),
        # shopName
        self.shopName=shopName
        # varchar(32),
        # avgScore
        self.avgScore=avgScore
        # varchar(32),
        # avePrice
        self.avePrice=avePrice
        # varchar(32),
        # address
        self.address=address
        # varchar(32),
        # phone
        self.phone=phone
        # varchar(32),
        # foods
        self.foods=foods
        # text,
        # Comments
        self.Comments=Comments
        # text);

    def __str__(self) -> str:
        # hoptype, shopId, shopName, avgScore, avePrice, address, phone, foods, Comments
       return "餐厅类型:%s\n餐厅id:%s\n餐厅名称:%s\n平均分数:%s\n平均价格:%s\n餐厅地址:%s\n订餐电话:%s\n菜单:%s\n评论:%s\n"%(self.shoptype,self.shopId,self.shopName,self.avgScore,self.avePrice,self.address,self.phone,self.foods,self.Comments)
class distance:
    def __init__(self,shopId1,shopName1,shopId2,shopName2,distance) -> None:
        # create
        # table
        # distance
        # (shopId1 varchar(32),
        self.shopId1=shopId1
        # shopName1
        self.shopName1=shopName1
        # varchar(32),
        # shopId2
        self.shopId2=shopId2
        # varchar(32),
        # shopName2
        self.shopName2=shopName2
        # varchar(32),
        # distance
        self.distance=distance
        # varchar(32));

class order:

    def __init__(self,account,shopname,ordertime) -> None:
        # create table Order1
        # (account varchar(32),
        self.account=account
        # shopname varchar(32),
        self.shopname=shopname
        # ordertime varchar(32));
        self.ordertime=ordertime

    def __str__(self) -> str:
        return "下单账号:"+str(self.account)+"  商店名称:"+str(self.shopname)+"  预定时间:"+str(self.ordertime)

