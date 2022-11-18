from DAO.shopUserDAO import shopUserDAO
from table import shopUser


class shopUserService:
    def __init__(self) -> None:
        self.DAO=shopUserDAO()

    # 登录验证
    def logI(self,shopUser):
        re=self.DAO.select(shopUser)
        return re

    # 注册
    def register(self):
        u=input("账号(shopid):")
        p=input("密码:")
        if u!="" and p!="":
            su=shopUser(u,p)
            re = self.DAO.insert(su)
            return re
        else:
            return False