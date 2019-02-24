# -*-coding:utf8-*-

from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
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
temp = 'http://quotes.money.163.com/hs/realtimedata/service/plate.php?host=/hs/realtimedata/service/plate.php&query=TYPE:HANGYE&fields=PLATE_ID,NAME,STOCK_COUNT&count=100&type=query'
req = urllib.request.Request(url=temp, headers=headers)

try:
    stockopen = urllib.request.urlopen(req)
    html =  str(stockopen.read())
    # qstr = '{"accessToken": "521de21161b23988173e6f7f48f9ee96e28", "User-Agent": "Apache-HttpClient/4.5.2 (Java/1.8.0_131)"}'
    # qstr = '{"page":0,"count":100,"order":-1,"total":47,"pagecount":1,"time":"2019-02-24 21:30:17","key":"\\/finance\\/hs\\/realtimedata\\/plate\\/19f9721cc1703e528ec70c3c85eed59a.json","list":[{"PLATE_ID":"hy015000","STOCK_COUNT":1,"RN":1,"NAME":""},{"PLATE_ID":"hy012001","STOCK_COUNT":53,"RN":2,"NAME":""},{"PLATE_ID":"hy019000","STOCK_COUNT":23,"RN":3,"NAME":""},{"PLATE_ID":"hy017000","STOCK_COUNT":10,"RN":4,"NAME":""},{"PLATE_ID":"hy013000","STOCK_COUNT":50,"RN":5,"NAME":""},{"PLATE_ID":"hy014000","STOCK_COUNT":49,"RN":6,"NAME":""},{"PLATE_ID":"hy016000","STOCK_COUNT":5,"RN":7,"NAME":""},{"PLATE_ID":"hy010000","STOCK_COUNT":122,"RN":8,"NAME":""},{"PLATE_ID":"hy003005","STOCK_COUNT":37,"RN":9,"NAME":""},{"PLATE_ID":"hy003002","STOCK_COUNT":43,"RN":10,"NAME":""},{"PLATE_ID":"hy003008","STOCK_COUNT":24,"RN":11,"NAME":""},{"PLATE_ID":"hy003009","STOCK_COUNT":30,"RN":12,"NAME":""},{"PLATE_ID":"hy003006","STOCK_COUNT":11,"RN":13,"NAME":""},{"PLATE_ID":"hy003007","STOCK_COUNT":8,"RN":14,"NAME":""},{"PLATE_ID":"hy003010","STOCK_COUNT":12,"RN":15,"NAME":""},{"PLATE_ID":"hy003012","STOCK_COUNT":16,"RN":16,"NAME":""},{"PLATE_ID":"hy003017","STOCK_COUNT":86,"RN":17,"NAME":""},{"PLATE_ID":"hy003019","STOCK_COUNT":67,"RN":18,"NAME":""},{"PLATE_ID":"hy003013","STOCK_COUNT":238,"RN":19,"NAME":""},{"PLATE_ID":"hy003016","STOCK_COUNT":74,"RN":20,"NAME":""},{"PLATE_ID":"hy003015","STOCK_COUNT":24,"RN":21,"NAME":""},{"PLATE_ID":"hy005000","STOCK_COUNT":99,"RN":22,"NAME":""},{"PLATE_ID":"hy003022","STOCK_COUNT":204,"RN":23,"NAME":""},{"PLATE_ID":"hy003023","STOCK_COUNT":133,"RN":24,"NAME":""},{"PLATE_ID":"hy003020","STOCK_COUNT":60,"RN":25,"NAME":""},{"PLATE_ID":"hy003021","STOCK_COUNT":137,"RN":26,"NAME":""},{"PLATE_ID":"hy003028","STOCK_COUNT":22,"RN":27,"NAME":""},{"PLATE_ID":"hy003026","STOCK_COUNT":344,"RN":28,"NAME":""},{"PLATE_ID":"hy003025","STOCK_COUNT":229,"RN":29,"NAME":""},{"PLATE_ID":"hy006000","STOCK_COUNT":173,"RN":30,"NAME":""},{"PLATE_ID":"hy002000","STOCK_COUNT":76,"RN":31,"NAME":""},{"PLATE_ID":"hy001000","STOCK_COUNT":42,"RN":32,"NAME":""},{"PLATE_ID":"hy004000","STOCK_COUNT":113,"RN":33,"NAME":""},{"PLATE_ID":"hy009000","STOCK_COUNT":267,"RN":34,"NAME":""},{"PLATE_ID":"hy007000","STOCK_COUNT":110,"RN":35,"NAME":""},{"PLATE_ID":"hy018000","STOCK_COUNT":57,"RN":36,"NAME":""},{"PLATE_ID":"hy008000","STOCK_COUNT":11,"RN":37,"NAME":""},{"PLATE_ID":"hy003004","STOCK_COUNT":41,"RN":38,"NAME":""},{"PLATE_ID":"hy003003","STOCK_COUNT":44,"RN":39,"NAME":""},{"PLATE_ID":"hy003018","STOCK_COUNT":33,"RN":40,"NAME":""},{"PLATE_ID":"hy003029","STOCK_COUNT":6,"RN":41,"NAME":""},{"PLATE_ID":"hy003027","STOCK_COUNT":45,"RN":42,"NAME":""},{"PLATE_ID":"hy003024","STOCK_COUNT":51,"RN":43,"NAME":""},{"PLATE_ID":"hy003011","STOCK_COUNT":14,"RN":44,"NAME":""},{"PLATE_ID":"hy011000","STOCK_COUNT":135,"RN":45,"NAME":""},{"PLATE_ID":"hy003014","STOCK_COUNT":219,"RN":46,"NAME":""},{"PLATE_ID":"hy003001","STOCK_COUNT":50,"RN":47,"NAME":""}]}'
    # print(html[0])
    # print(html[1])
    # print(html[2])
    # print(html[3])
    # print(qstr)
    # print(qstr[0])
    # print(qstr[1])
    # print(qstr[2])
    # print(qstr[3])
    # print(html[2:-1])
    # print(html)
    # htmljson = json.loads(qstr)
    htmljson = json.loads(html[2:-1])
    platelist = htmljson.get('list')
    print(platelist)
    print(platelist[0])
    print(platelist[1])
    print(platelist[2])
    for item in platelist:
        print(item)
    listposi = html.find('list')
    for i in range(177, 210):
        print(platelist[i])
    print(htmljson[0])
    print(htmljson[1])
    print(htmljson[2])
    print(htmljson[3])
    print(platelist)
    # print(htmljson)
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    # tag = soup.find('table', {'class': "ID_table stocks-info-table"})
    tag = soup.find('table', {'class': "table_bg001 border_box limit_sale"})
    print(tag)
    data = tag.find_all('td')
    stockopen.close()
    print(data)
    sub = 0
    alllen = len(data)
except urllib.error.URLError as e:
    if hasattr(e, 'code'):
        print("%(stock)06d HTTPError "%{'stock':stnum})
        print(e.code)
    elif hasattr(e, 'reason'):
        print("%(stock)06d URLError"%{'stock':stnum})
        print(e.reason)
print(stocklist)

def restoreNumber(numStr):
    pattern=re.compile('\D')
    numList=pattern.split(numStr)
    numStr=''.join(numList)
    # print(int(numStr))
    return numStr

def spider(stnum):
    stockplate = 0
    # print(type(stnum))
    if (stnum >= 730000) and (stnum < 731000):#沪市新股
        stockplate = 0
    elif (stnum >= 700000) and (stnum < 701000):#沪市配股
        stockplate = 0
    elif (stnum >= 600000) and (stnum < 600200):#沪市A股
        stockplate = 0
    elif (stnum >= 300000) and (stnum < 301000):#创业板股票
        stockplate = 0
    elif (stnum >= 80000) and (stnum < 81000):#沪市A股
        stockplate = 0
    elif (stnum >= 2000) and (stnum < 3000):#中小板股票
        stockplate = 0
    elif (stnum < 1000):#深市A股
        stockplate = 0
    else:
        return
    #打开数据库连接
    db= pymysql.connect(host="localhost",user="pytest",
        password="pytest123",db="stock",port=3306)
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # stnum = 2402
    # for stnum in range(300000, 301000):#创业板股票
    # for stnum in range(2000, 3000):#中小板股票
    # for stnum in range(600000, 602000):#沪市A股票
    try:
        # sql = 'select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA=' + 
        cur.execute("select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA=\'stock\' and TABLE_NAME=\'%(stock)06d\'"%{'stock' : stnum}) 	#执行sql语句
        results = cur.fetchall()	#获取查询的所有记录
        if results:
            print(results)
        else:
            print("not table for %(stock)06d ;"%{'stock' : stnum})
            temp = "CREATE TABLE IF NOT EXISTS `%(stock)06d` (\
            `Date` varchar(32) NOT NULL,\
            `StockPlate` varchar(4) NOT NULL,\
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
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"%{'stock':stnum}
            cur.execute(temp) 	#执行sql语句
            results = cur.fetchall()	#获取查询的所有记录
            if results:
                print(results)
    except Exception as e:
        raise e
    # finally:
    #     db.close()	#关闭连接
    minyea = 2016
    mydate = datetime.now()
    yea = mydate.year
    sea = (mydate.month - 1) // 3 + 1
    # nowyea = datetime.now().year
    # for yea in range(nowyea, minyea, -1):
        # for sea in range(1, 5):
    while yea > minyea:
        while sea > 0:
            # temp = 'http://quotes.money.163.com/trade/lsjysj_002402.html?year=2019&season=1'
            temp = "http://quotes.money.163.com/trade/lsjysj_%(stock)06d.html?year=%(year)d&season=%(season)d"%{'stock':stnum, 'year':yea, 'season':sea}
            print("request url is %(urll)s"%{'urll' : temp})
            req = urllib.request.Request(url=temp, headers=headers)
            
            try:
                stockopen = urllib.request.urlopen(req)
                html =  stockopen.read()
                soup = BeautifulSoup(html, 'lxml')
                tag = soup.find('table', {'class': "table_bg001 border_box limit_sale"})
                data = tag.find_all('td')
                stockopen.close()

                sub = 0
                alllen = len(data)
                while sub < alllen:
                    # break;
                    temp = """INSERT INTO `%(stock)06d` \
                        (Date, StockPlate, OpenPrice, HighPrice, LowPrice, ClosePrice, DiffrenceValue, DiffrencePercent, Amplitude, Volume, Amount, HandRate) \
                    VALUES \
                        ('%(Date)s', '%(StockPlate)s', '%(OpenPrice)s', '%(HighPrice)s', '%(LowPrice)s', '%(ClosePrice)s', '%(DiffrenceValue)s', '%(DiffrencePercent)s', '%(Amplitude)s','%(Volume)s', '%(Amount)s', '%(HandRate)s');""" \
                        %{'stock':stnum,'StockPlate':stockplate,'Date':data[sub].text,'OpenPrice':data[sub+1].text,'HighPrice':data[sub+2].text,'LowPrice':data[sub+3].text,'ClosePrice':data[sub+4].text,\
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
            except urllib.error.URLError as e:
                if hasattr(e, 'code'):
                    print("%(stock)06d HTTPError "%{'stock':stnum})
                    print(e.code)
                elif hasattr(e, 'reason'):
                    print("%(stock)06d URLError"%{'stock':stnum})
                    print(e.reason)
                sea -= 1
                yea = minyea
                continue
            sea -= 1
        yea -= 1
        if(sea == 0):
            sea = 4
        if yea <= minyea:
            db.close()	#关闭连接y
            break

    


pool = ThreadPool(10)
# results = pool.map(spider, stocklist)
try:
    results = pool.map(spider, stocklist)
except Exception as e:
    # print 'ConnectionError'
    print (e)
    time.sleep(300)
    results = pool.map(spider, stocklist)
    print(results)

# db.close()	#关闭连接y
print("spider over")
pool.close()
pool.join()