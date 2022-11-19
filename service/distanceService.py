from DAO.distanceDAO import distanceDAO
from DAO.shopDAO import shopDAO


class distanceService:
    def __init__(self) -> None:
        self.DAO=distanceDAO()


class node:
    def __init__(self, totalDis, pre, dis) -> None:
        self.totalDis =totalDis # 总距离
        self.pre  =pre# 前一个点的距离
        self.dis  =dis# 和前一个点的距离
        self.isVisite = False  # 默认没有被访问


class Gra:
    def __init__(self, origin) -> None:  # E为所有节点的集合,n为总节点数量
        self.edges = []  # 领接
        self.S = {}  # 字典,存放节点
        self.origin = origin  # 起点的id
        s=shopDAO().selectShopByID(origin)
        if len(s)==0:
            print("启动失败!原因可能是:id无效或者数据库无效!")
            raise Exception("")
        self.DAO=distanceDAO()

    def getData(self):
        # 查询数据库,为edges和n赋值
        self.edges=self.DAO.selectAlltoEdge()
        # 测试
        # def __init__(self, shop1, shop2, distance) -> None:
        #     self.s1 = shop1
        #     self.s2 = shop2
        #     self.d = distance




        # 根据起点id初始化字典
        pass

    def Dijkstra(self):
        j = 0
        pop=[]
        for i in self.edges:
            isPop = False
            if i.s1 == self.origin:
                # def __init__(self, totalDis, pre, dis)
                self.S[i.s2] = node(i.d, self.origin, i.d)
                isPop = True
            if i.s2 == self.origin:
                self.S[i.s1] = node(i.d, self.origin, i.d)
                isPop = True
            # 去除无效边,如果i这条边已经添加到字典中,说明这条边是无效边了,减少后续迭代次数
            if isPop:
                pop.append(j)
            j+=1

        for i in range(len(pop)):
            self.edges.pop(pop[len(pop)-1-i])

        pop.clear()
        # 最小距离
        while True:
            minid = ""
            min = 10000000000
            for k in self.S.keys():
                tempN = self.S[k]
                if not tempN.isVisite and tempN.totalDis < min:
                    min=tempN.totalDis
                    minid = k

            if minid != "":  # 找到最小距离
                self.S[minid].isVisite = True
                # 更新字典
                j = 0
                for i in self.edges:
                    isPop = False
                    if i.s1 == minid:
                        # def __init__(self, totalDis, pre, dis)
                        try:  # 尝试去找i.s2这个点,没有报异常
                            n = self.S[i.s2]
                            if n.totalDis>min+i.d:
                                n.totalDis=min+i.d
                                n.pre=minid
                        except:
                            self.S[i.s2]=node(min+i.d, minid, i.d)
                        isPop = True
                    if i.s2 == minid:
                        try:  # 尝试去找i.s2这个点,没有报异常
                            n = self.S[i.s1]
                            if n.totalDis > min + i.d:
                                n.totalDis = min + i.d
                                n.pre = minid
                        except:
                            self.S[i.s1] = node(min+i.d, minid, i.d)
                        isPop = True
                    # 去除无效边,如果i这条边已经添加到字典中,说明这条边是无效边了,减少后续迭代次数
                    if isPop:
                        pop.append(j)
                    j+=1
                for i in range(len(pop)):
                    self.edges.pop(pop[len(pop)-1-i])
                pop.clear()
            else:  # 说明全部都已经访问了
                return

