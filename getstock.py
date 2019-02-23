# -*-coding:utf8-*-

from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import time
import sys
import re
import json
import MySQLdb
from bs4 import BeautifulSoup
# import urllib as ur

import urllib.request
import pymysql  #导入 pymysql
from datetime import datetime


# python2重载utf-8
# reload(sys)
# sys.setdefaultencoding('utf-8')

# python3默认utf-8
# import importlib
# importlib.reload(sys)

# id av cid title tminfo time click danmu coins favourites duration honor_click honor_coins honor_favourites
# mid name article fans tags[3] common

# temp = """INSERT INTO `%(table)s` \
#     (Date, OpenPrice, HighPrice, LowPrice, ClosePrice, DiffrenceValue, DiffrencePercent, Amplitude, Volume, Amount, HandRate) \
# VALUES \
#     (%(Date)s, %(OpenPrice).02f, %(HighPrice).02f, %(LowPrice).02f, %(ClosePrice).02f, %(DiffrenceValue).02f, %(DiffrencePercent).02f, %(Amplitude).02f, %(Volume)s, %(Amount)s, %(HandRate).02f);""" \
#     %{'table':'23456','Date':data[sub].text,'OpenPrice':float(data[sub+1].text),'HighPrice':float(data[sub+2].text),'LowPrice':float(data[sub+3].text),'ClosePrice':float(data[sub+4].text),\
#         'DiffrenceValue':float(data[sub+5].text),'DiffrencePercent':float(data[sub+6].text),'Amplitude':float(data[sub+9].text),\
#         'Volume':restoreNumber(data[sub+7].text),'Amount':restoreNumber(data[sub+8].text),'HandRate':float(data[sub+10].text)}
urls = []

#打开数据库连接
db= pymysql.connect(host="localhost",user="pytest",
 	password="pytest123",db="stock",port=3306)
# 使用cursor()方法获取操作游标
cur = db.cursor()

for i in range(2402, 2403):
    # url = 'http://bilibili.com/video/av' + str(i)
    url = 'http://quotes.money.163.com/trade/lsjysj_00' + str(i) +'.html?year=2019&season=1'
    urls.append(url)

def restoreNumber(numStr):
    pattern=re.compile('\D')
    numList=pattern.split(numStr)
    numStr=''.join(numList)
    # print(int(numStr))
    return numStr

def spider(url):
    try:
        # sql = 'select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA=' + 
        cur.execute('select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA=\'stock\' and TABLE_NAME=\'002403\'') 	#执行sql语句
        results = cur.fetchall()	#获取查询的所有记录
        if results:
            print(results)
        else:
            print('not table for 002403')
            temp = "CREATE TABLE IF NOT EXISTS `%(stocknumber)06d` (\
            `Date` varchar(32) NOT NULL,\
            `OpenPrice` varchar(8) NOT NULL,\
            `HighPrice` varchar(8) NOT NULL,\
            `LowPrice` varchar(8) NOT NULL,\
            `ClosePrice` varchar(8) NOT NULL,\
            `DiffrenceValue` varchar(8) NOT NULL,\
            `DiffrencePercent` varchar(8) NOT NULL,\
            `Amplitude` varchar(8) NOT NULL,\
            `Volume` bigint(20) NOT NULL,\
            `Amount` bigint(20) NOT NULL,\
            `HandRate` varchar(8) NOT NULL,\
            PRIMARY KEY (`Date`)\
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"%{'stocknumber':2402}
            cur.execute(temp) 	#执行sql语句
            results = cur.fetchall()	#获取查询的所有记录
            if results:
                print(results)
    except Exception as e:
        raise e
    # finally:
    #     db.close()	#关闭连接

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/2010010 Firefox/62.0'}
    for yea in range(2008, 2019):
        for sea in range(1, 5):
            # temp = 'http://quotes.money.163.com/trade/lsjysj_002402.html?year=2019&season=1'
            temp = "http://quotes.money.163.com/trade/lsjysj_%(stock)06d.html?year=%(year)d&season=%(season)d"%{'stock':2402, 'year':yea, 'season':sea}
            print(temp)
            req = urllib.request.Request(url=temp, headers=headers)
            html = urllib.request.urlopen(req).read()
            soup = BeautifulSoup(html, 'lxml')
            tag = soup.find('table', {'class': "table_bg001 border_box limit_sale"})
            data = tag.find_all('td')

            sub = 0
            alllen = len(data)
            while sub < alllen:
                temp = """INSERT INTO `%(table)06d` \
                    (Date, OpenPrice, HighPrice, LowPrice, ClosePrice, DiffrenceValue, DiffrencePercent, Amplitude, Volume, Amount, HandRate) \
                VALUES \
                    ('%(Date)s', '%(OpenPrice)s', '%(HighPrice)s', '%(LowPrice)s', '%(ClosePrice)s', '%(DiffrenceValue)s', '%(DiffrencePercent)s', '%(Amplitude)s','%(Volume)s', '%(Amount)s', '%(HandRate)s');""" \
                    %{'table':2402,'Date':data[sub].text,'OpenPrice':data[sub+1].text,'HighPrice':data[sub+2].text,'LowPrice':data[sub+3].text,'ClosePrice':data[sub+4].text,\
                        'DiffrenceValue':data[sub+5].text,'DiffrencePercent':data[sub+6].text,'Amplitude':data[sub+9].text,\
                        'Volume':restoreNumber(data[sub+7].text),'Amount':restoreNumber(data[sub+8].text),'HandRate':data[sub+10].text}
                # print(temp)
                sub += 11
                try:
                    cur.execute(temp) 	#执行sql语句
                    # cur.execute("INSERT INTO `23456` (Date, OpenPrice, HighPrice, LowPrice, ClosePrice, DiffrenceValue, DiffrencePercent, Amplitude, Volume, Amount, HandRate) VALUES (2019-02-22, 7.70, 8.05, 7.69, 8.00, 0.29, 3.76, 4.67, 240900, 18995, 2.89)") 	#执行sql语句
                    results = cur.fetchall()	#获取查询的所有记录
                    if results:
                        print(results)
                    db.commit()
                except Exception as e:
                    db.rollback() 
    


pool = ThreadPool(10)
# results = pool.map(spider, urls)
try:
    results = pool.map(spider, urls)
except Exception as e:
    # print 'ConnectionError'
    print (e)
    time.sleep(300)
    results = pool.map(spider, urls)

db.close()	#关闭连接
pool.close()
pool.join()