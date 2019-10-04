# -*-coding:utf8-*-

from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor, as_completed
from functools import partial
# import requests
import time
# import sys
import re
# import json
# import MySQLdb
from bs4 import BeautifulSoup
# import urllib as ur

import socket
import urllib.request
import urllib.error
import urllib
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

stocklist = {}

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/2010010 Firefox/62.0'}
# temp = 'http://quotes.money.163.com/trade/lsjysj_002402.html?year=2019&season=1'
# temp = "http://quotes.money.163.com/old/#query=leadIndustry&DataType=industryPlate&sort=PERCENT&order=desc&count=100&page=0"
# temp = 'http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQA&fields=NO%2CSYMBOL%2CNAME&sort=PERCENT&order=desc&count=3600&type=query'
temp = 'http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQA&fields=NAME%2CSYMBOL&count=5000&type=query'
req = urllib.request.Request(url=temp, headers=headers)

# abs_dir = "F:\\code\\demo\\python\\pymysql\\log.txt"
abs_dir = os.path.dirname(os.path.abspath(__file__)) + '\\amarket_log.txt'
print(abs_dir)
logfp = open(abs_dir, "w")
logfp.write("start the A market get data program at %(time)s\n"%{'time' : time.strftime("%H:%M:%S")})

try:
    stockopen = urllib.request.urlopen(req, timeout=10)
    html =  str(stockopen.read())
    # print(html)
    htmljson = json.loads(html[2:-1])
    # print(htmljson)
    sortstocklist = htmljson.get('list')
    # print(platelist)
    stocklist = sorted(sortstocklist,key = lambda e:e.__getitem__('SYMBOL'))
    for item in stocklist:
        # print(item)
        logfp.write("%(item)s\n"%{'item':str(item)})
    # snum = 0
    # for item in codelist:
    #     stocklist[snum] = item
    #     snum += 1
        # print(str(stocklist['snum']))
        # logfp.write("%(item)s\n"%{'item':str(item)})
    #     # print(item)
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
except socket.timeout as e:
    print (type(e) )
        
# print(type(stocklist[0]))
# print(type(stocklist))
# print(sorted(stocklist.items(), key=lambda d:d[1], reverse = True))
# print(sorted({'NO':i['NO'] for i in stocklist}.items(), key=lambda a: a[1]))
# print(sorted(stocklist.items(), key=lambda x: x[1][0], reverse=True))
# print(sorted(stocklist,key = lambda e:e.__getitem__('NO')))

def restoreNumber(numStr):
    pattern=re.compile('\D')
    numList=pattern.split(numStr)
    numStr=''.join(numList)
    # print(int(numStr))
    return numStr
def get_day_type(query_date):
    url = "http://tool.bitefu.net/jiari/?d=%(day)s"%{'day' : query_date}
    # temp = "http://tool.bitefu.net/jiari/?d=%(day)s"%{'day' : query_date}
    
    try:
        req = urllib.request.Request(url=url, headers=headers)
        stockopen = urllib.request.urlopen(req, timeout=10)
        content =  stockopen.read()
        stockopen.close()
        if content:
            try:
                day_type = int(content)
            except ValueError:
                return -1
            else:
                return day_type
        else:
            return -1
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print("%(stock)s get_day_type "%{'stock':url})
            logfp.write("%(stock)s get_day_type \n"%{'stock':url})
            # print(e.code)
        elif hasattr(e, 'reason'):
            print("%(stock)s get_day_type"%{'stock':url})
            logfp.write("%(stock)s get_day_type\n"%{'stock':url})
        return -1
    except socket.timeout as e:
        print (type(e) )
        return -1

 
 
def is_tradeday(query_date):
    weekday = datetime.strptime(query_date, '%Y%m%d').isoweekday()
    if weekday <= 5 and get_day_type(query_date) == 0:
        return 1
    else:
        return 0
 

def spider(stnum):#, update):
    # print(stnum)
    # print(update)
    dbcount = 0
    update = 1
    stockplate = 0
    #打开数据库连接
    db= pymysql.connect(host="localhost",user="pytest",
        password="pytest123",db="stock",port=3306, charset='utf8')
    dbcount += 1
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    
    name = stnum['NAME'].encode('utf-8').decode('unicode_escape')
    # name = "国农科技"
    try:
        temp = "select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA=\'stock\' and TABLE_NAME=\'%(stock)s(%(name)s)\'"%{'stock' : stnum['SYMBOL'], 'name' : name} 	#执行sql语句
        print(temp)    
        cur.execute(temp) 	#执行sql语句
        results = cur.fetchall()	#获取查询的所有记录
        # print(results)
        if results:
            print(results)
        else:
            print("creat table for %(stock)s(%(name)s) ;"%{'stock' : stnum['SYMBOL'], 'name' : name})
            logfp.write("creat table for %(stock)s(%(name)s) ;"%{'stock' : stnum['SYMBOL'], 'name' : name})
            temp = "CREATE TABLE IF NOT EXISTS `%(stock)s(%(name)s)` (\
            `Date` varchar(32) NOT NULL,\
            `StockPlate` varchar(8) NOT NULL,\
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
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"%{'stock':stnum['SYMBOL'], 'name' : name}
            cur.execute(temp) 	#执行sql语句
            results = cur.fetchall()	#获取查询的所有记录
            if results:
                print(results)
    except Exception as e:
        raise e
    finally:
        db.close()	#关闭连接
        dbcount -= 1

    #打开数据库连接
    db= pymysql.connect(host="localhost",user="pytest",
        password="pytest123",db="stock",port=3306)
    dbcount += 1
    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    
    # temp = 'select * from `%(stock)s(%(name)s)` where Date="%(nian)d-%(yue)02d-%(ri)02d"'%{'stock':stnum['SYMBOL'], 'name' : name, 'nian': yea, 'yue' : 3*sea, 'ri' : day}
    temp = 'select Date from `%(stock)s(%(name)s)`'%{'stock':stnum['SYMBOL'], 'name' : name}
    print(temp)
    cur.execute(temp) 	#执行sql语句
    sqldate = cur.fetchall()	#获取查询的所有记录

    # if sqldate:
    #     # print(sqldate)
    #     for dateitem in sqldate:
    #         print(dateitem)

    minyea = 2010
    mydate = datetime.now()
    yea = mydate.year
    sea = (mydate.month - 1) // 3 + 1
    datetemp = '20190928'
    
    while yea > minyea:
        logfp.write("%(stock)s(s) inserinfo in %(temp)d\n"%{'stock':stnum['SYMBOL'],'temp' : yea})
        # logfp.write("%(stock)s(%(name)s) inserinfo in %(temp)d\n"%{'stock':stnum['SYMBOL'], 'name' : name,'temp' : yea})
        while sea > 0:
            if sea == 1 or sea == 4:
                day = 31
            else:
                day = 30
            while day > 0:
                datestr = "%(nian)d%(yue)02d%(ri)02d"%{'nian': yea, 'yue' : 3*sea, 'ri' : day}
                datetemp = datestr[:4] + '-' + datestr[4:6] + '-' + datestr[6:]
                if(is_tradeday(datestr) == 1):
                    break
                day -= 1
            nodate = 0
            for dateitem in sqldate:
                print(dateitem[0])
                if dateitem[0] == datetemp:
                # print("%(datetemp)s == %(datetemp)s")
                    print("%(stock)s :%(date1)s count :%(count)d "%{'stock':stnum['SYMBOL'], 'date1': datetemp,'count': dbcount})
                    nodate = 1
                    break
            if nodate:
                sea -= 1
                continue
                
            # temp = 'http://quotes.money.163.com/trade/lsjysj_002402.html?year=2019&season=1'
            temp = "http://quotes.money.163.com/trade/lsjysj_%(stock)s.html?year=%(year)d&season=%(season)d"%{'stock':stnum['SYMBOL'], 'year':yea, 'season':sea}
            print("url is %(urll)s\t"%{'urll' : temp})
            # logfp.write("request url is %(urll)s\n"%{'urll' : temp})
            req = urllib.request.Request(url=temp, headers=headers)
            
            try:
                stockopen = urllib.request.urlopen(req, timeout=10)
                html =  stockopen.read()
                if html:
                    soup = BeautifulSoup(html, 'lxml')
                if soup:
                    tag = soup.find('table', {'class': "table_bg001 border_box limit_sale"})
                if tag:
                    data = tag.find_all('td')
                stockopen.close()

                sub = 0
                alllen = len(data)
                if alllen == 0:
                    yea = minyea
                    break
                while sub < alllen:
                    # break;
                    temp = """REPLACE INTO `%(stock)s(%(name)s)` \
                        (Date, StockPlate, OpenPrice, HighPrice, LowPrice, ClosePrice, DiffrenceValue, DiffrencePercent, Amplitude, Volume, Amount, HandRate) \
                    VALUES \
                        ('%(Date)s', '%(StockPlate)s', '%(OpenPrice)s', '%(HighPrice)s', '%(LowPrice)s', '%(ClosePrice)s', '%(DiffrenceValue)s', '%(DiffrencePercent)s', '%(Amplitude)s','%(Volume)s', '%(Amount)s', '%(HandRate)s');""" \
                        %{'stock':stnum['SYMBOL'], 'name' : name,'StockPlate':stockplate,'Date':data[sub].text,'OpenPrice':data[sub+1].text,'HighPrice':data[sub+2].text,'LowPrice':data[sub+3].text,'ClosePrice':data[sub+4].text,\
                            'DiffrenceValue':data[sub+5].text,'DiffrencePercent':data[sub+6].text,'Amplitude':data[sub+9].text,\
                            'Volume':restoreNumber(data[sub+7].text),'Amount':restoreNumber(data[sub+8].text),'HandRate':data[sub+10].text,'Date1':data[sub].text}
                    # print(temp)
                    # logfp.write("%(stock)s(%(name)s) inserinfo is %(temp)s\n"%{'stock':stnum['SYMBOL'], 'name' : name,'temp' : temp[230:]})
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
            except urllib.error.URLError as e:
                if hasattr(e, 'code'):
                    print("%(stock)s HTTPError "%{'stock':stnum['SYMBOL']})
                    logfp.write("%(stock)s HTTPError \n"%{'stock':stnum['SYMBOL']})
                    # print(e.code)
                elif hasattr(e, 'reason'):
                    print("%(stock)s URLError"%{'stock':stnum['SYMBOL']})
                    logfp.write("%(stock)s URLError\n"%{'stock':stnum['SYMBOL']})
                    # print(e.reason)
                sea -= 1
                yea = minyea
                continue
            except socket.timeout as e:
                print (type(e) )
                continue
            sea -= 1
            if(update):
                if(yea <= minyea):
                    update -= 1
                if(update == 0):
                    yea = minyea
                    break
        yea -= 1
        if(sea == 0):
            sea = 4
        if yea <= minyea:
            db.close()	#关闭连接y
            dbcount -= 1
            # logfp.write("%(stock)s(%(name)s) over in %(nian)d%(yue)02d%(ri)02d at %(time)s\n"%{'stock':stnum['SYMBOL'], 'name' : name,'nian': yea, 'yue' : 3*sea, 'ri' : day,'time' : time.strftime("%H:%M:%S")})
            logfp.flush()
            break

# print(sortstocklist)
# for item in sortstocklist:
#     print(item)

if __name__ == '__main__':    
    pool = ThreadPoolExecutor(max_workers=1)
    task_list = []
    for taskitem in stocklist:
#        if(taskitem['SYMBOL'] < '000001' ):
        if(int(str(taskitem['SYMBOL']), 10) < 0 ):
            print(taskitem['SYMBOL'])
            continue
        task_list.append(pool.submit(spider, taskitem))
    # task_list = [pool.submit(spider, taskitem) for taskitem in stocklist]
    for result in as_completed(task_list):
        # task_name = task_map.get(result)
        print(result)

# if __name__ == '__main__':    
#     pool = ProcessPoolExecutor(max_workers=8)
#     try:
#         results = list(pool.map(partial(spider,update=0),sorted(stocklist,key = lambda e:e.__getitem__('SYMBOL'))))
#         # results = list(pool.map(spider, sorted(stocklist,key = lambda e:e.__getitem__('SYMBOL'))))
#     except Exception as e:
#         # print 'ConnectionError'
#         print (e)
#         time.sleep(300)
#         results = list(pool.map(partial(spider,update=0),sorted(stocklist,key = lambda e:e.__getitem__('SYMBOL'))))
#         # results = list(pool.map(spider, sorted(stocklist,key = lambda e:e.__getitem__('SYMBOL'))))
#         print(results)
#         logfp.write("ThreadPool exception\n")
#     print("spider over time")
#     logfp.write("spider over\n")
#     logfp.close()

# pool = ThreadPool(1)
# # results = pool.map(spider, stocklist)
# try:
#     # results = list(pool.map(partial(spider,update=1),sorted(stocklist,key = lambda e:e.__getitem__('SYMBOL'))))
#     # results = pool.map(spider, sorted(stocklist,key = lambda e:e.__getitem__('NO')))
#     results = pool.map(spider, sortstocklist)
# except Exception as e:
#     # print 'ConnectionError'
#     print (e)
#     time.sleep(300)
#     # results = list(pool.map(partial(spider,update=0),sorted(stocklist,key = lambda e:e.__getitem__('SYMBOL'))))
#     # results = pool.map(spider, sorted(stocklist,key = lambda e:e.__getitem__('NO')))
#     results = pool.map(spider, sortstocklist)
#     print(results)
#     logfp.write("ThreadPool exception\n")
# pool.close()
# pool.join()
# print("spider over time")
# logfp.write("spider over\n")
# logfp.close()

    # pool = threadpool.ThreadPool(2)
    # requests = threadpool.makeRequests(hello, func_var)
    # [pool.putRequest(req) for req in requests]
    # pool.wait()
