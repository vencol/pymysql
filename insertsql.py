import pymysql
#2.插入操作
db= pymysql.connect(host="localhost",user="pytest",
 	password="pytest123",db="py1",port=3306)
 
# 使用cursor()方法获取操作游标
cur = db.cursor()
 
# sql_insert ="""insert into user(id,name,password) values(489,'liu','1234')"""
# sql_insert ="""insert into user(id,name,password) values(46,'liu','1234')"""
sql_insert ="""INSERT INTO `stock`             (Date, OpenPrice, HighPrice, LowPrice, ClosePrice, DiffrenceValue, DiffrencePercent, Amplitude, Volume, Amount, HandRate)         VALUES             ('2019-02-22', '7.70', '8.05', '7.69', '8.00', '0.29', '3.76', '4.67','240900', '18995', '2.89');"""
# cur.execute("INSERT INTO `23456` (Date, OpenPrice, HighPrice, LowPrice, ClosePrice, DiffrenceValue, DiffrencePercent, Amplitude, Volume, Amount, HandRate) VALUES (2019-02-22, 7.70, 8.05, 7.69, 8.00, 0.29, 3.76, 4.67, 240900, 18995, 2.89)") 	#执行sql语句
 
try:
	print(sql_insert)
	cur.execute(sql_insert)
	#提交
	db.commit()
except Exception as e:
	#错误回滚
	db.rollback() 
finally:
	db.close()