from DAO.userDAO import userDAO
from table import user


class userService:
    def __init__(self) -> None:
        self.DAO=userDAO()

    def deleteByUsername(self,username):
        return self.DAO.deleteUser(username)

    def selectByUsername(self,username):
        return self.DAO.selectUserByAccount(username)

    def selectAll(self):
        return self.DAO.selectAll()

    # 登录验证:根据账号查询
    def logI(self, user):
        return self.DAO.select(user)

    # 注册
    def register(self):
        #检测账号密码是否为空
        a=input("注册账号:")
        p=input("注册密码:")
        c=input("联系方式:")
        if a !="" and p !="":
            us=user(a,p,c)
            if us is not None and us.account is not None and us.password:
                return self.DAO.insert(us)
        return False

    def updateInfor(self,me2):
        if me2 is not None and me2.password is not None and me2.password !="":
            self.DAO.updateUserPassword(me2.account,me2.password)
        if me2 is not None and me2.contact is not None and me2.contact !="":
            self.DAO.updateUserContact(me2.account,me2.contact)
        return True

    def deleteUser(self,me):
        if me is not None and me.account is not None and me.account !="":
            self.DAO.deleteUser(me.account)