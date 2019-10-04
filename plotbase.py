import pymysql  #导入 pymysql

import matplotlib.pyplot as plt

fig,ax = plt.subplots()
plt.xlabel('migration speed (MB/s)')
plt.ylabel('migration time (s); request delay (ms)')
yticks = range(-100,100,10)
ax.set_yticks(yticks)
 
#打开数据库连接
db= pymysql.connect(host="localhost",user="pytest",
    password="pytest123",db="stock",port=3306)
 
# 使用cursor()方法获取操作游标
cur = db.cursor()
 
#1.查询操作
# 编写sql 查询语句  user 对应我的表名 
sql = "select `Date`, `DiffrencePercent`,`Volume`, `Amplitude`, `HandRate` from `600226(瀚叶股份)`"
Date=[]
DiffrencePercent=[]
Volume=[]
Amplitude=[]
HandRate=[]
data = []
xa = range(0,429, 1)
xaaa = 0
try:
	cur.execute(sql) 	#执行sql语句
	results = cur.fetchall()	#获取查询的所有记录
	print("Date","DiffrencePercent","Volume","Amplitude","HandRate")
    # pritnt(type(results))
	for row in results :
        xaaa+=1
		DiffrencePercent.append(row[1])
		Amplitude.append(row[3])
		HandRate.append(row[4])
		# name = row[1]
		# password = row[2]
		# print(row[0], row[1], row[2], row[3], row[4])
    

    
except Exception as e:
	raise e
finally:
	db.close()	#关闭连接


plt.plot(xa,DiffrencePercent,"x-",label="DiffrencePercent")
plt.plot(xa,Amplitude,"+-",label="Amplitude")
plt.plot(xa,HandRate,"*-",label="HandRate")

plt.grid(True)
plt.legend(bbox_to_anchor=(1.0, 1), loc=1, borderaxespad=0.005)
plt.show()
