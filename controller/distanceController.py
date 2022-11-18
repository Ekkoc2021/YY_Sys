from service.distanceService import distanceService

class distanceController:
    def __init__(self) -> None:
        self.Service=distanceService();
        # 餐馆查询
        # 餐馆信息保存在文件shop.txt中，
        # 文件中的ID和餐馆名称均是唯一的，因此将餐馆名称作为查找的关键。
        # 若该餐馆存在，则返回餐馆的基本信息，以及用户到该餐馆的最短距离。


        # 41508471
        # 砂锅米线（矿大北门店） 1659250
        # 颐香园家常菜（颐和园店） 9.143
        # 以砂锅米线为起点,图为非负带权图,采用迪杰斯特拉算法
        # 从数据库中遍历所有的边==><e1,e2,dis>==>找到起始边<e1,e2,dis>==>路径图==>
