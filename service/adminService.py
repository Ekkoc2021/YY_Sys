from DAO.adminDAO import adminDAO


class adminService:
    def __init__(self) -> None:
        self.DAO=adminDAO()

    # 登录验证
    def logI(self, admin):
        re = self.DAO.select(admin)
        return re