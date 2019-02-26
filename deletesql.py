import pymysql
#4.删除操作
db= pymysql.connect(host="localhost",user="pytest",
 	password="pytest123",db="py1",port=3306)
 
# 使用cursor()方法获取操作游标
cur = db.cursor()


# str1 ='更符合地方'
# str2 = '\\u4e2d\\u56fd\\u7535\\u53fa'
# str3 = str2.encode('utf-8').decode('unicode_escape')
# print(str1)
# print(str2.encode('utf-8').decode('unicode_escape'))
# print(str3)
# temp = "CREATE TABLE IF NOT EXISTS `%(stock)s` (\
# `Date` varchar(32) NOT NULL,\
# PRIMARY KEY (`Date`)\
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"%{'stock':str3}
# cur.execute(temp) 	#执行sql语句
# db.close()
 
sql_delete ="delete from user where id = %d"
 
try:
	cur.execute(sql_delete % (3))  #像sql语句传递参数
	#提交
	db.commit()
except Exception as e:
	#错误回滚
	db.rollback() 
finally:
	db.close()