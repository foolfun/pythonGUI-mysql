import pymysql

 
##如果数据表已经存在使用execute()方法删除表
#cursor.execute("drop table if EXISTS income")
 
#创建数据库SQL语句
#time,ironincome,general_income,baiincome
#SQL1 = """CREATE TABLE `income` (
#  `id` int(11) NOT NULL AUTO_INCREMENT,
#  `datetime` varchar(20) DEFAULT NULL,
#  `ironincome` decimal(20,2) DEFAULT NULL,
#  `generalincome` decimal(20,2) DEFAULT NULL,
#  `baiincome` decimal(20,2) DEFAULT NULL,
#  PRIMARY KEY (`id`)
#) ENGINE=InnoDB DEFAULT CHARSET=utf8;
#"""

# 打开数据库
db = pymysql.connect(host='localhost',port =3306,user='root',passwd='zsl123',db='login_users',charset='utf8' )
 
#使用cursor()方法获取操作游标
cursor = db.cursor()
SQL = """CREATE DATABASE `login_users`"""

SQL1 = """DROP TABLE IF EXISTS `stu_info`"""


SQL2 = """CREATE TABLE `stu_info` (
  `id` varchar(32) NOT NULL COMMENT '学号',
  `stu_name` varchar(32) NOT NULL COMMENT '姓名',
  `stu_major` varchar(32) NOT NULL COMMENT '专业',
  `stu_class` varchar(32) NOT NULL COMMENT '班级',
  `card_num` varchar(32) NOT NULL COMMENT '银行卡号',
  `stu_scholarship` enum('是','否') NOT NULL COMMENT '奖学金有无',
  `stu_scholarship_status` enum('是','否') NOT NULL COMMENT '奖学金发放情况',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;
"""
#使用innodb引擎，数据库默认编码为utf-8


SQL3 = """LOCK TABLES `stu_info` WRITE"""
SQL4 = """ALTER TABLE `stu_info` DISABLE KEYS"""
SQL5 = """INSERT INTO `stu_info` VALUES (1,'测试姓名1','男',20,'000001','Python01','测试联系方式1'),(2,'测试姓名2','男',23,'000002','Python02','测试联系方式2'),(3,'测试姓名3','女',21,'000003','Python03','测试联系方式3'),(4,'测试姓名4','男',28,'000004','php01','测试联系方式4'),(5,'测试姓名5','男',30,'000005','php02','测试联系方式5'),(6,'测试姓名6','女',25,'000006','php03','测试联系方式6'),(7,'测试姓名7','男',35,'000007','JavaScript01','测试联系方式7'),(8,'测试姓名8','男',31,'000008','JavaScript02','测试联系方式8'),(9,'测试姓名9','女',26,'000009','JavaScript03','测试联系方式9'),(10,'测试姓名10','男',24,'000010','SQL01','测试联系方式10');"""
SQL6 = """ALTER TABLE `stu_info` ENABLE KEYS"""
SQL7 = """UNLOCK TABLES;"""

SQL8 = """DROP TABLE IF EXISTS `users`;"""
SQL9 = """CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `user_name` varchar(32) NOT NULL COMMENT '用户名',
  `user_password` varchar(23) NOT NULL COMMENT '登录密码',
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_name` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
"""

SQL10 = """LOCK TABLES `users` WRITE;"""

SQL11 = """INSERT INTO `users` VALUES (1,'admin','Python09'),(2,'momobaba','123456');"""

SQL12 = """UNLOCK TABLES;"""

#cursor.execute(SQL) 
#cursor.execute(SQL1)
#cursor.execute(SQL2)
#cursor.execute(SQL3)
#cursor.execute(SQL4)
#cursor.execute(SQL5)
#cursor.execute(SQL6)
#cursor.execute(SQL7)
#cursor.execute(SQL8)
#cursor.execute(SQL9)
#cursor.execute(SQL10)
#cursor.execute(SQL11)

db.close()