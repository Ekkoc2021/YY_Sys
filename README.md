#          **丫丫餐馆管理信息系统**  

  大二第一个学期python数据结构的结课作业，要求设计一个订餐管理系统。可以用数据库？？？？？数据结构结课作业？？？

## 1,使用

### 1.1 建表语句

```mysql
create database yyordersystem;
use  yyordersystem;
# 建表语句 管理员表Cancel changes
create table admin (username char(32) primary key, password char(32) not null);

# 距离表:
# shopId,shopname是外键,每条数据对应着数据库中无向带权图的边
create table distance (shopId1 varchar(32) not null,
shopName1 varchar(32) not null,
shopId2 varchar(32) not null,
shopName2 varchar(32) not null,
distance double not null);

#订单表:
# account 用户账号order1,shopname 商店名称,ordertime:插入格式必须是xxxx-xx-xx-xx-xx-xx(xxxx-xx-xx xx:xx:xx)
create table order1 (account varchar(32) not null,shopname varchar(32) not null,ordertime datetime not null);

#商店表:插入商店表必须保证在商店用户表(shopuser)有对应用户数据
create table shop
(shoptype varchar(32) not null,shopId varchar(32) primary key,
shopName varchar(32) not null,avgScore double,avePrice double not null,
address varchar(32) not null,phone varchar(32) not null,foods text not null,Comments text);

insert into yyordersystem.shop value(
"北京小吃快餐","41508471"," 砂锅米线（矿大北门店）",5,16,
"海淀区学院路中国矿业大学北门弘彧大厦院内豫香缘黄焖鸡米饭隔壁",
"15711107678",
"food_id: 157129460, food_name: 砂锅米线, food_price: 0
food_id: 144368653, food_name: 芝麻烧饼, food_price: 2
food_id: 105060183, food_name: 豆芽, food_price: 4
food_id: 105060204, food_name: 鱼豆腐, food_price: 5
food_id: 105060196, food_name: 金针菇, food_price: 4
food_id: 41049460, food_name: 菌类锅, food_price: 15
food_id: 135009336, food_name: 单加米线, food_price: 4
food_id: 105060184, food_name: 豆皮, food_price: 4
food_id: 111459570, food_name: 亲亲肠, food_price: 5
food_id: 222236112, food_name: 香菇丸蔬菜砂锅米线, food_price: 24
food_id: 222235763, food_name: 鱼豆腐蔬菜砂锅米线, food_price: 24
food_id: 229622085, food_name: 肉夹馍, food_price: 5
food_id: 222234634, food_name: 腊肠菌类砂锅米线, food_price: 26
food_id: 222234019, food_name: 肥羊菌类砂锅米线, food_price: 26
food_id: 222233182, food_name: 肥牛菌类砂锅米线, food_price: 23
food_id: 222230771, food_name: 蟹肉棒菌类砂锅米线, food_price: 26
food_id: 111460667, food_name: 银耳, food_price: 5
food_id: 111460391, food_name: 木耳, food_price: 5
food_id: 105060185, food_name: 鹌鹑蛋, food_price: 4
food_id: 111460801, food_name: 牛肉丸, food_price: 5
food_id: 8338557, food_name: 菌類米線, food_price: 0
food_id: 222237011, food_name: 腊肉蔬菜砂锅米线, food_price: 24
food_id: 222236580, food_name: 鸡肉蔬菜砂锅米线, food_price: 24
food_id: 222236397, food_name: 肥牛蔬菜砂锅米线, food_price: 24
food_id: 152133925, food_name: 普通锅, food_price: 14
food_id: 105060206, food_name: 桂花肠, food_price: 5
food_id: 105060205, food_name: 墨鱼丸, food_price: 5
food_id: 105060201, food_name: 虾丸, food_price: 5
food_id: 105060195, food_name: 平菇, food_price: 4
food_id: 105060189, food_name: 土豆片, food_price: 4
food_id: 105060186, food_name: 大白菜, food_price: 4
food_id: 105060181, food_name: 油麦菜, food_price: 4
food_id: 135008744, food_name: 甜不辣, food_price: 5
food_id: 266469592, food_name: 鲍汁脆皮萝卜, food_price: 2.9
food_id: 243040405, food_name: 鲁西牛肉辣酱, food_price: 6
food_id: 233511733, food_name: 辣椒油, food_price: 0.6
food_id: 229627087, food_name: 雪花啤酒, food_price: 5
food_id: 229385333, food_name: 蛋炒饭, food_price: 24
food_id: 229385245, food_name: 怡寶矿泉水, food_price: 3
food_id: 228066855, food_name: 原味手抓饼, food_price: 5
food_id: 222237043, food_name: 培根蔬菜砂锅米线, food_price: 24
food_id: 222236977, food_name: 亲亲肠蔬菜砂锅米线, food_price: 24
food_id: 222236552, food_name: 火腿蔬菜砂锅米线, food_price: 24
food_id: 222236528, food_name: 牛肉丸蔬菜砂锅米线, food_price: 24
food_id: 222236497, food_name: 腊肉菌类砂锅米线, food_price: 26
food_id: 222236464, food_name: 蟹棒蔬菜砂锅米线, food_price: 24
food_id: 222236120, food_name: 腊肠蔬菜砂锅米线, food_price: 24
food_id: 222235917, food_name: 方便面, food_price: 3
food_id: 222235911, food_name: 土豆粉, food_price: 5
food_id: 222235854, food_name: 五花肉蔬菜砂锅米线, food_price: 24
","Comment0: 满满的食欲感
Comment1: 味道很淡了，几乎是没什么口味。
Comment2: 挺好「#套餐：单人普通锅套餐」
Comment3: 用餐体验还好，就是人有点多因为在美食广场里
Comment4: 不错啊
Comment5: 地方太不好找了，绕了好几圈才找到的！味道还好吧！总感觉一股草味儿
Comment6: 服务态度超级差，味道一般般，尤其是很不卫生，以后再也不会去吃了！让人恶心！肉夹馍都馊了还拿来卖，无良商家。
Comment7: 一般吧没觉得多么好吃，材料也不多
Comment8: 我没有收到米线！也没有看见订单！就直接显示待评价！我也不知道怎么回事！
Comment9: 在一个类似于取外卖的那种地方。
");

#商店用户表:username对应着shopid,
create table shopuser(username varchar(32) primary key,password varchar(32) not null);
insert into yyordersystem.shopuser value("41508471", "1241508471");

#用户表
create table user(account varchar(32) primary key, password varchar(32) not null,contact varchar(32) not null);

```

### 1.2 修改配置文件

找到db.ini,修改配置

```ini
[db]
# 主机ip
host=localhost
# 数据库名称
database=YYOrderSystem
# 连接数据库账号
user=root
# 连接数据库密码
password=qwe456654.
#端口号
port=3306

[location]
#当前位置id,通过shopid定位当前位置,比如当前位置在矿大,使用矿大某个餐厅的id,请确保数据库shop中有该id
id=41508471
```

### 1.3 启动

找到main.py,运行,提示'可以正常使用'配置正常

