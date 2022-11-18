from controller.orderController import orderController
from controller.shopController import shopController
from controller.userController import userController
from service.adminService import adminService
from service.distanceService import Gra
from service.shopUserService import shopUserService
from service.userService import userService
import threading
import time
from table import user, shopUser, admin

userService01 = userService()
shopUserService01 = shopUserService()
admin01 = adminService()
userController01 = userController()
shopController01=shopController()
orderController01=orderController()

g=Gra("1")
isOK=[False]
class boot:

    def job(self):
        #开始计算最短距离
        g.getData()
        time.sleep(5)
        g.Dijkstra()
        isOK[0]=True
    def newThread(self):
        # 考虑到实际数据数量太大,为了不影响体验,为计算最短距离开启一个线程,这个计算是程序启动就开始的
        new_thread = threading.Thread(target=self.job, name="T1")
        # 启动
        new_thread.start()


    def log(self,c):
        username = input("-------------------\n账号:")
        pw = input("密码:")
        if username != "" and pw != "":
            if c == "1":
                return userService01.logI(user(username, pw, None))
            elif c == "2":
                return shopUserService01.logI(shopUser(username, pw))
            elif c == "3":
                return admin01.logI(admin(username, pw))
        return None

    def run(self):
        while 0 == 0:
            print("-------------------\n欢迎使用YY订餐系统\n1,用户\n2,商家\n3,管理员\n4,退出\n-------------------")
            c = input("请输入选项:")
            print("-------------------")
            if c == "1":
                # 用户
                while 0 == 0:
                    print("用户登录界面\n1,登录\n2,注册\n3,返回\n-------------------")
                    c2 = input("请输入:")
                    if c2 == "1":
                        u = self.log(c)
                        if u is not None and u.account is not None and u.password is not None:
                            print("-------------------\n登录成功!\n欢迎用户:" + u.account)
                            while True:
                                uc = input("-------------------\n1,个人信息管理\n2,餐馆查询\n3,我的预定\n4,餐馆推荐\n5,返回\n")
                                if uc == "1":
                                    # 注销账户要求退出用户
                                    if userController01.InforManage(u):
                                        break
                                elif uc == "2":
                                    shopController01.GMapping(g,isOK[0])

                                elif uc == "3":
                                    orderController01.manageOrder(u)
                                # 预定
                                # 一个用户可以预订多家餐馆，一个餐馆也可被多个用户预订，为了简化处理，所有预订信息均保存在用户订餐信息文件order.txt中。
                                # 查询用户所有预订selectByUserAccount。查询用户本人的所有预订信息，可能包含多个餐馆的预订。
                                # 查询某餐馆selectByShopName。通过输的餐馆名称，查询该用户在该餐馆的预订信息。
                                # 添加预订insert。输入餐馆的名称，如果该餐馆在文件shop.txt中存在

                                elif uc == "4":
                                    shopController01.recommend()
                                elif uc == "5":
                                    break
                        else:
                            print("密码或者用户名错误!\n-------------------")
                    elif c2 == "2":
                        if userService01.register():
                            print("注册成功!,快去登录吧!")
                        else:
                            print("用户名称重复!")
                    elif c2 == "3":
                        break

            # 商家----------------------------------------
            elif c == "2":
                while 0 == 0:
                    print("商家登录界面\n1,登录\n2,注册\n3,返回\n-------------------")
                    c2 = input("请输入:")
                    if c2 == "1":
                        u = self.log(c)
                        if u is not None and u.username is not None and u.password is not None:
                            print("-------------------\n登录成功!")
                            while True:
                                c2=input("-------------------\n欢迎商户:" + u.username+"\n1,餐馆信息管理\n2,餐馆预定管理\n3,返回\n")
                                if c2=="1":
                                    if shopController01.manageShopInfor(u):
                                        break
                                elif c2=="2":
                                    orderController01.manageShopOrder(u)
                                elif c2=="3":
                                    break

                        else:
                            print("密码或者用户名错误!\n-------------------")
                    elif c2 == "2":
                        if shopController01.register():
                            print("注册成功!,快去登录吧!")
                        else:
                            print("注册失败,注册信息都不能为空,换个id试试!")
                    elif c2 == "3":
                        break
            # 管理员---------------------------------------
            elif c == "3":
                # 管理员
                while 0 == 0:
                    print("管理员登录界面\n1,登录\n2,注册\n3,返回\n-------------------")
                    c2 = input("请输入:")
                    if c2 == "1":
                        u = self.log(c)
                        if u is not None and u.username is not None and u.password is not None:
                            print("-------------------\n登录成功!\n欢迎管理员:" + u.username)
                            while True:
                                c2=input("1,用户管理\n2,商家管理\n3,返回\n-------------------\n")
                                if c2=="1":
                                    userController01.userManage()
                                elif c2=="2":
                                    shopController01.shopUserManage()
                                elif c2=="3":
                                    break
                        else:
                            print("密码或者用户名错误!\n-------------------")
                    elif c2 == "2":
                        print("请联系系统管理员申请后台账号!(●￣(ｴ)￣●)\n-------------------")
                    elif c2 == "3":
                        break
            elif c == "4":
                break
            else:
                print("请重新输入")
