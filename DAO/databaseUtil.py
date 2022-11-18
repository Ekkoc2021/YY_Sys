import pymysql

def getC():
    return pymysql.connect(
        host="localhost",
        database="YYOrderSystem",
        user="root",
        password="qwe456654.",
        port=3306,
)