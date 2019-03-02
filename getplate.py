# -*-coding:utf8-*-

from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor
# import requests
import time
# import sys
import re
# import json
# import MySQLdb
from bs4 import BeautifulSoup
# import urllib as ur

import urllib.request
import urllib.error
import pymysql  #导入 pymysql
from datetime import datetime 
import json
import os


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
stocklist = []

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/2010010 Firefox/62.0'}
# temp = 'http://quotes.money.163.com/trade/lsjysj_002402.html?year=2019&season=1'
# temp = "http://quotes.money.163.com/old/#query=leadIndustry&DataType=industryPlate&sort=PERCENT&order=desc&count=100&page=0"
temp = 'http://quotes.money.163.com/old/#query=hy003019&DataType=HS_RANK&sort=PERCENT&order=desc&count=24&page=0'
req = urllib.request.Request(url=temp, headers=headers)

# abs_dir = "F:\\code\\demo\\python\\pymysql\\log.txt"
abs_dir = os.path.dirname(os.path.abspath(__file__)) + '\\plate_log.txt'
print(abs_dir)
logfp = open(abs_dir, "w")
logfp.write("start the plate get data program\n")

try:
    stockopen = urllib.request.urlopen(req)
    html =  stockopen.read()
    soup = BeautifulSoup(html, 'lxml')
    hynum = 0
    while hynum < 100:
        idtemp = str(soup.find(id = 'f0-f6-f%(hynum)d'%{'hynum' : hynum}))
        stlen = idtemp.find('qid=')
        if stlen > 0:
            # print(idtemp[stlen + 5 : stlen + 13])
            tag = soup.find('li', {'id': 'f0-f6-f%(hynum)d'%{'hynum' : hynum}})
            stag = idtemp[stlen + 5 : stlen + 13] + ("(%(name)s)"%{'name' : tag.text[1:]})
            stocklist.append(stag)
            logfp.write("stocklist[%(hynum)d] = %(item)s\n"%{'hynum' : hynum, 'item':stag})
        else:
            break
        hynum += 1
    logfp.flush()
    stockopen.close()
except urllib.error.URLError as e:
    if hasattr(e, 'code'):
        # print("%(stock)06d HTTPError "%{'stock':stnum})
        print("e.code")
        print(e.code)
    elif hasattr(e, 'reason'):
        # print("%(stock)06d URLError"%{'stock':stnum})
        print("e.reason")
        print(e.reason)
    logfp.write("urllib.error.URLError")
        
# print(stocklist[0])
# print(stocklist)

def restoreNumber(numStr):
    pattern=re.compile('\D')
    numList=pattern.split(numStr)
    numStr=''.join(numList)
    # print(int(numStr))
    return numStr

def spider(stnumlist):
    #打开数据库连接
    db= pymysql.connect(host="localhost",user="pytest",
        password="pytest123",db="stock",port=3306)
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    
    print(stnumlist)
    print(stnumlist[9:-1])
    stnum = stnumlist[0:8]
    name = stnumlist[9:-1]
    # name = stnum['NAME'].encode('utf-8').decode('unicode_escape')
    try:
        # sql = 'select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA=' + 
        temp = "select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA=\'stock\' and TABLE_NAME=\'%(stock)s(%(name)s)\'"%{'stock' : stnum, 'name' : name} 	#执行sql语句
        print(temp)
        cur.execute(temp) 	#执行sql语句
        results = cur.fetchall()	#获取查询的所有记录
        print(results)
        if results:
            print(results)
        else:
            print("creat table for %(stock)s(%(name)s) ;"%{'stock' : stnum, 'name' : name})
            logfp.write("creat table for %(stock)s(%(name)s) ;"%{'stock' : stnum, 'name' : name})
            temp = "CREATE TABLE IF NOT EXISTS `%(stock)s(%(name)s)` (\
            `Code` varchar(8) NOT NULL,\
            `StockPlate` varchar(16) NOT NULL,\
            `Cname` varchar(32) NOT NULL,\
            `Price` varchar(8) NOT NULL,\
            `FlowMarket` varchar(16) NOT NULL,\
            `AllMarker` varchar(16) NOT NULL,\
            `Profit` varchar(16) NOT NULL,\
            `Revenue` varchar(16) NOT NULL,\
            PRIMARY KEY (`Code`)\
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"%{'stock':stnum, 'name' : name}
            cur.execute(temp) 	#执行sql语句
            results = cur.fetchall()	#获取查询的所有记录
            if results:
                print(results)
    except Exception as e:
        raise e
    
            # temp = 'http://quotes.money.163.com/trade/lsjysj_002402.html?year=2019&season=1'
    temp = 'http://quotes.money.163.com/hs/service/diyrank.php?host=http://quotes.money.163.com/hs/service/diyrank.php&page=0&query=PLATE_IDS:%(hy)s&fields=NO,SYMBOL,NAME,PRICE,PERCENT,UPDOWN,FIVE_MINUTE,OPEN,YESTCLOSE,HIGH,LOW,VOLUME,TURNOVER,HS,LB,WB,ZF,PE,MCAP,TCAP,MFSUM,MFRATIO.MFRATIO2,MFRATIO.MFRATIO10,SNAME,CODE,ANNOUNMT,UVSNEWS&sort=PERCENT&order=desc&count=380&type=query'%{'hy':stnum}
    print("request url is %(urll)s"%{'urll' : temp})
    logfp.write("request url is %(urll)s\n"%{'urll' : temp})
    req = urllib.request.Request(url=temp, headers=headers)

    try:

        stockopen = urllib.request.urlopen(req)
        html =  str(stockopen.read())
        # print(html)
        htmljson = json.loads(html[2:-1])
        # print(htmljson)
        hylist = htmljson.get('list')
        for item in hylist:
            # print(item['SYMBOL'])
            # print("%(item)s\n"%{'item':str(item)})
            logfp.write("%(item)s\n"%{'item':str(item)})
            logfp.flush()

            

        # sub = 0
        # alllen = len(data)
        # while sub < alllen:
            # break;
            temp = """INSERT INTO `%(stock)s(%(name)s)` \
                (Code, StockPlate, Cname, Price, FlowMarket, AllMarker, Profit, Revenue) \
            VALUES \
                ('%(Code)s', '%(StockPlate)s', '%(Cname)s', '%(Price)s', '%(FlowMarket)s', '%(AllMarker)s','%(Profit)s', '%(Revenue)s');""" \
                %{'stock':stnum, 'name' : name,'Code':item['SYMBOL'],'StockPlate':stnum,'Cname':item['NAME'].encode('utf-8').decode('unicode_escape'),\
                    'Price':item['PRICE'],'FlowMarket':item['MCAP'],'AllMarker':item['TCAP'],'Profit':item['MFRATIO']['MFRATIO2'],'Revenue':item['MFRATIO']['MFRATIO10']}
            print(temp)
            logfp.write("inserinfo is %(temp)s\n"%{'temp' : temp})
            try:
                cur.execute(temp) 	#执行sql语句
                # cur.execute("INSERT INTO `23456` (Date, OpenPrice, HighPrice, LowPrice, ClosePrice, DiffrenceValue, DiffrencePercent, Amplitude, Volume, Amount, HandRate) VALUES (2019-02-22, 7.70, 8.05, 7.69, 8.00, 0.29, 3.76, 4.67, 240900, 18995, 2.89)") 	#执行sql语句
                results = cur.fetchall()	#获取查询的所有记录
                if results:
                    print(results)
                db.commit()
            except Exception as e:
                db.rollback() 
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print("%(stock)s HTTPError "%{'stock':stnum})
            logfp.write("%(stock)s HTTPError \n"%{'stock':stnum})
            # print(e.code)
        elif hasattr(e, 'reason'):
            print("%(stock)s URLError"%{'stock':stnum})
            logfp.write("%(stock)s URLError\n"%{'stock':stnum})
            # print(e.reason)
    db.close()	#关闭连接y

    

if __name__ == '__main__':    
    pool = ProcessPoolExecutor(max_workers=16)
    try:
        results = list(pool.map(spider, stocklist))
    except Exception as e:
        # print 'ConnectionError'
        print (e)
        time.sleep(300)
        results = list(pool.map(spider, stocklist))
        print(results)
        logfp.write("ThreadPool exception\n")
    print("spider over time")
    logfp.write("spider over\n")
    logfp.close()

# pool = ThreadPool(1)
# # results = pool.map(spider, stocklist)
# try:
#     results = pool.map(spider, stocklist)
# except Exception as e:
#     # print 'ConnectionError'
#     print (e)
#     time.sleep(300)
#     results = pool.map(spider, stocklist)
#     print(results)
#     logfp.write("ThreadPool exception\n")

# # db.close()	#关闭连接y
# print("spider over")
# logfp.write("spider over\n")
# logfp.close()
# pool.close()
# pool.join()