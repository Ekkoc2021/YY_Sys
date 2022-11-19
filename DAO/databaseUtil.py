import pymysql
import configparser
file = 'db.ini'
def getDBInf():
    con = configparser.ConfigParser()
    con.read(file, encoding='utf-8')
    # 获取特定section
    db1 = con.items('db') 	# 返回结果为元组
    # 可以通过dict方法转换为字典
    return dict(db1)
def getLocation():
    con = configparser.ConfigParser()
    con.read(file, encoding='utf-8')
    # 获取特定section
    location= con.items('location')  # 返回结果为元组
    # 可以通过dict方法转换为字典
    return dict(location)["id"]
def getC():
    db=getDBInf()
    return pymysql.connect(
        host=db["host"],
        database=db["database"],
        user=db["user"],
        password=db["password"],
        port=eval(db["port"])
)