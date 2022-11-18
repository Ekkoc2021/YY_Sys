from service.userService import userService
from table import user


class userController:
    def __init__(self,service=None) -> None:
        if service is not None:
            self.Service=service
        else:
            self.Service=userService()

    def showAllUser(self):
        userList=self.Service.selectAll()
        for i in userList:
            print(i.__str__())

    def userManage(self):
        while True:
            uc2 =input("-------------------\n1,查看所有用户\n2,查询用户\n3,删除账户\n4,返回\n-------------------\n")
            if uc2 == "1":
                self.showAllUser()
                pass
            elif uc2 == "2":
                username=input("用户账号:")
                user=self.Service.selectByUsername(username)
                if user is not None:
                    print(user)
                else:
                    print("没有此用户!")
            elif uc2 == "3":
                username = input("用户账号:")
                if self.Service.deleteByUsername(username):
                    print("删除用户成功!")
                else:
                    print("删除失败,数据库中没有该用户,或者其他原因,请重试!")
            elif uc2 == "4":
                return False


    def InforManage(self,me):
        while True:
            uc2 = input("-------------------\n1,查看个人信息\n2,修改个人信息\n3,注销账户\n4,返回\n-------------------\n")
            if uc2=="1":
                self.myInformation(me)
            elif uc2=="2":
                self.updateMyInformation(me)
                return True
            elif uc2=="3":
                self.Service.deleteUser(me)
                return True
            elif uc2=="4":
                return False


    def myInformation(self,me):
        # 查看个人信息user。查找该用户信息，然后将该用户的账号和联系方式显示出来。
        try:
            print("我的账号:%s\n我的联系方式:%s" %(me.account,me.contact))
        except:
            print("网络错误或者其他")

    def updateMyInformation(self,me):
        # 修改个人信息user。用户可以对自己的个人信息进行修改，包括密码和联系方式，将修改后的信息存储到文件user.txt中。
        p=input("密码(不修改则直接回车):")
        c=input("联系方式(不修改则直接回车):")
        me2 = user(me.account, p,c)
        self.Service.updateInfor(me2)
