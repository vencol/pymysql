# -*-coding:utf8-*-
# http://quotes.money.163.com/service/chddata.html?code=1002714&start=20140117&end=20190927&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP

# 沪深AB
# http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQA&fields=NO%2CSYMBOL%2CNAME%2CPRICE%2CPERCENT%2CUPDOWN%2CFIVE_MINUTE%2COPEN%2CYESTCLOSE%2CHIGH%2CLOW%2CVOLUME%2CTURNOVER%2CHS%2CLB%2CWB%2CZF%2CPE%2CMCAP%2CTCAP%2CMFSUM%2CMFRATIO.MFRATIO2%2CMFRATIO.MFRATIO10%2CSNAME%2CCODE%2CANNOUNMT%2CUVSNEWS&sort=PERCENT&order=desc&count=24&type=query
# http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQB&fields=NO%2CSYMBOL%2CNAME%2CPRICE%2CPERCENT%2CUPDOWN%2CFIVE_MINUTE%2COPEN%2CYESTCLOSE%2CHIGH%2CLOW%2CVOLUME%2CTURNOVER%2CHS%2CLB%2CWB%2CZF%2CPE%2CMCAP%2CTCAP%2CMFSUM%2CMFRATIO.MFRATIO2%2CMFRATIO.MFRATIO10%2CSNAME%2CCODE%2CANNOUNMT%2CUVSNEWS&sort=PERCENT&order=desc&count=24&type=query
# 沪深A排序
# http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQA&fields=NO%2CSYMBOL%2CNAME%2CPRICE%2CPERCENT%2CUPDOWN%2CFIVE_MINUTE%2COPEN%2CYESTCLOSE%2CHIGH%2CLOW%2CVOLUME%2CTURNOVER%2CHS%2CLB%2CWB%2CZF%2CPE%2CMCAP%2CTCAP%2CMFSUM%2CMFRATIO.MFRATIO2%2CMFRATIO.MFRATIO10%2CSNAME%2CCODE%2CANNOUNMT%2CUVSNEWS&sort=SYMBOL&order=asc&count=24&type=query
# 沪A深A
# http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQA%3BEXCHANGE%3ACNSESH&fields=NO%2CSYMBOL%2CNAME%2CPRICE%2CPERCENT%2CUPDOWN%2CFIVE_MINUTE%2COPEN%2CYESTCLOSE%2CHIGH%2CLOW%2CVOLUME%2CTURNOVER%2CHS%2CLB%2CWB%2CZF%2CPE%2CMCAP%2CTCAP%2CMFSUM%2CMFRATIO.MFRATIO2%2CMFRATIO.MFRATIO10%2CSNAME%2CCODE%2CANNOUNMT%2CUVSNEWS&sort=PERCENT&order=desc&count=24&type=query
# http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQA%3BEXCHANGE%3ACNSESZ&fields=NO%2CSYMBOL%2CNAME%2CPRICE%2CPERCENT%2CUPDOWN%2CFIVE_MINUTE%2COPEN%2CYESTCLOSE%2CHIGH%2CLOW%2CVOLUME%2CTURNOVER%2CHS%2CLB%2CWB%2CZF%2CPE%2CMCAP%2CTCAP%2CMFSUM%2CMFRATIO.MFRATIO2%2CMFRATIO.MFRATIO10%2CSNAME%2CCODE%2CANNOUNMT%2CUVSNEWS&sort=PERCENT&order=desc&count=24&type=query
# 沪B深B
# http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQB%3BEXCHANGE%3ACNSESH&fields=NO%2CSYMBOL%2CNAME%2CPRICE%2CPERCENT%2CUPDOWN%2CFIVE_MINUTE%2COPEN%2CYESTCLOSE%2CHIGH%2CLOW%2CVOLUME%2CTURNOVER%2CHS%2CLB%2CWB%2CZF%2CPE%2CMCAP%2CTCAP%2CMFSUM%2CMFRATIO.MFRATIO2%2CMFRATIO.MFRATIO10%2CSNAME%2CCODE%2CANNOUNMT%2CUVSNEWS&sort=PERCENT&order=desc&count=24&type=query
# http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQB%3BEXCHANGE%3ACNSESZ&fields=NO%2CSYMBOL%2CNAME%2CPRICE%2CPERCENT%2CUPDOWN%2CFIVE_MINUTE%2COPEN%2CYESTCLOSE%2CHIGH%2CLOW%2CVOLUME%2CTURNOVER%2CHS%2CLB%2CWB%2CZF%2CPE%2CMCAP%2CTCAP%2CMFSUM%2CMFRATIO.MFRATIO2%2CMFRATIO.MFRATIO10%2CSNAME%2CCODE%2CANNOUNMT%2CUVSNEWS&sort=PERCENT&order=desc&count=24&type=query


import os
import time
import datetime 

import json
import socket
import urllib
import urllib.error
import urllib.request


# import numpy as np
# import tushare as ts
#         opendaylist = ts.trade_cal()
import pandas as pd
# pd.set_option('display.max_rows',None)
# pd.set_option('display.max_rows',1000)
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor, as_completed, wait, ALL_COMPLETED,FIRST_COMPLETED


# config data
g_needUpdateMarket  = 0
g_stockBeginDate    = '2008-01-01'
g_stockOpenDatePath = '\\.tradday.csv'    
g_dbName            = 'bstock'

print("%(st)s"%{'st' : g_stockBeginDate.replace('-', '')})

# global struct
g_pdSortStockList   = pd.DataFrame()

# 在Windows下经常用python open函数的人相信都遇到过UnicodeDecodeError: ‘gbk’ codec…这种编码问题。而且很多有经验的人应该知道解决方法是加上参数encoding=“utf-8”，因为"utf-8"是更通用的编码：
import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])

# logfileimport _locale
datapath = os.path.dirname(os.path.abspath(__file__))
logpath = datapath + '\\000002amarket_log.txt'
print(logpath)
logfp = open(logpath, "w")
logfp.write("start the A market get data program at %(time)s\n"%{'time' : time.strftime("%H:%M:%S")})
begintime = time.time()
datapath = datapath + "\\csvdata"
if (os.path.exists(datapath) == False):
    os.makedirs(datapath)

g_stockDataPath = datapath + "\\data.csv"
if (os.path.exists(g_stockDataPath) == False):
    file = open(g_stockDataPath, 'w')
    file.close()

# http://file.tushare.org/tsdata/calAll.csv
g_stockOpenDatePath = datapath + g_stockOpenDatePath
if (os.path.exists(g_stockOpenDatePath) == False):
    temp = "http://file.tushare.org/tsdata/calAll.csv"
    try:
        urllib.request.urlretrieve(temp, g_stockOpenDatePath)
    except socket.timeout:
        count = 1
        while count <= 5:
            try:
                urllib.request.urlretrieve(temp, g_stockOpenDatePath)                                              
                break
            except socket.timeout:
                err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
                print(err_info)
                count += 1
        if count > 5:
            print("download job failed!\n")
g_pdTraDay = pd.read_csv(g_stockOpenDatePath)
# print(g_pdTraDay.loc[g_pdTraDay['calendarDate'] == '2019-10-01'] )

def getMarket(market):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/2010010 Firefox/62.0'}
    if (market == 'A') or (market == 'B'):#AB股
        temp = "http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQ" + \
                market + "&fields=NO%2CNAME%2CSYMBOL%2CVOLUME&sort=SYMBOL&order=asc&count=5000&type=query"
    else:
        if (market[:2] == 'SH') or (market[:2] == 'SZ'):
            if (market[-1] == 'A') or (market[-1] == 'B'):
                temp = "http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQ" + \
                        market[-1] + "%3BEXCHANGE%3ACNSE" + market[:2] + "&fields=NO%2CNAME%2CSYMBOL%2CVOLUME&sort=SYMBOL&order=asc&count=5000&type=query"
        else:
            if (market == 'KCB'):#科创板
                temp = "http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQA" + \
                        "%3BKSH%3Atrue%3BNODEAL%3Afalse&fields=NO%2CNAME%2CSYMBOL%2CVOLUME&sort=SYMBOL&order=asc&count=5000&type=query"
            else:
                if (market == 'CYB'):#创业板
                    temp = "http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQA" + \
                            "%3BGEM%3Atrue%3BNODEAL%3Afalse&fields=NO%2CNAME%2CSYMBOL%2CVOLUME&sort=SYMBOL&order=asc&count=5000&type=query"
    print(temp)
    req = urllib.request.Request(url=temp, headers=headers)
    try:
        stockopen = urllib.request.urlopen(req, timeout=10)
        html =  str(stockopen.read())
        htmljson = json.loads(html[2:-1])
        sortstocklist = htmljson.get('list')
        for stdict in sortstocklist:
            stdict['NAME'] = stdict['NAME'].encode('utf-8').decode('unicode_escape').lower().replace('*', '_')
            # print(stdict['NAME'])
        # print(sortstocklist)
        # amarkettype = np.dtype([("NAME", np.str_, 20), ("SYMBOL", np.str_, 6), ("NO", np.int32),("PRICE", np.float32)])
        pdSortStockList = pd.DataFrame(sortstocklist)#, dtype=amarkettype)
        # del pdSortStockList['PRICE']
        del pdSortStockList['NO']
        pdSortStockList.rename(columns={'PRICE':'DATE'},inplace=True) 
        # pdSortStockList = pdSortStockList.set_index(pdSortStockList['SYMBOL'])
        # print(pdSortStockList)
        # print(pdSortStockList.head(50))
        stockopen.close()

        # metadata=MetaData(engine)
        # market=Table('000000amarket',metadata, 
        #             Column('name',String(20)),
        #             Column('date',String(20)),
        #             Column('volume',Integer),
        #             Column('number',String(20),primary_key=True))
        # metadata.create_all()

        # print(pdSortStockList)
        # pd.io.sql.to_sql(pdSortStockList, '000000amarket',con=engine, if_exists='replace', index=False)
        # pdSortStockList.to_sql('000000amarket',con=engine, if_exists='replace', index=False)  
        g_pdSortStockList.to_csv(g_stockDataPath, index=False) 
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print("e.code")
            print(e.code)
        elif hasattr(e, 'reason'):
            print("e.reason")
            print(e.reason)
        logfp.write("urllib.error.URLError\n")
    except socket.timeout as e:
        print (type(e) )
    return pdSortStockList

# database
db_info = {'user':'pytest',  
    'password':'pytest123',  
    'host':'localhost',  
    'database': g_dbName  # 这里我们事先指定了数据库，后续操作只需要表即可
}      
engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s/%(database)s?charset=utf8' % db_info,encoding='utf-8')    #这里直接使用pymysql连接,echo=True，会显示在加载数据库所执行的SQL语句。
# data = pd.read_sql_query("select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA=\'%(db)s\' and TABLE_NAME=\'000000amarket\'"%{'db' : g_dbName},con = engine)

print(os.path.getsize(g_stockDataPath))
if (os.path.getsize(g_stockDataPath) > 13096):
    g_pdSortStockList = pd.read_csv(g_stockDataPath)#, encoding='gbk')
    if(g_pdSortStockList.empty):
    # if(1):
        g_pdSortStockList = getMarket('A')
    else:
        # g_pdSortStockList = pd.read_sql_query('select * from `000000Amarket`',con = engine)
        if g_pdSortStockList.empty:
            g_pdSortStockList = getMarket('A')
else:
    g_pdSortStockList = getMarket('A')
    
# pd.set_option('display.max_rows',None)#max_colwidth
# logfp.write(str(g_pdSortStockList[ g_pdSortStockList[ 'DATE'].isnull() ] ))
# logfp.flush()
# logfp.write("all of the stocklist is all of the stocklist is all of the stocklist is all of the stocklist is:\n")
# logfp.flush()
# logfp.write(str(g_pdSortStockList[ g_pdSortStockList[ 'DATE'].isnull() == False] ))
# logfp.flush()

# logfp.write("%(symbol)s \n"%{'symbol':g_pdSortStockList.sort_index})
# logfp.write("all of the stocklist is all of the stocklist is all of the stocklist is all of the stocklist is:\n")
# logfp.flush()
pd.set_option('display.max_rows',None)#max_colwidth
g_pdSortStockList = g_pdSortStockList.sort_values(by='DATE', ascending=False).reset_index(drop=True, inplace=False)
logfp.write("%(symbol)s \n"%{'symbol':g_pdSortStockList})
logfp.flush()
pd.set_option('display.max_rows',10 )
print(g_pdSortStockList)

# print(g_pdSortStockList.loc[g_pdSortStockList.index.size - 1]['SYMBOL'])
# print(type(g_pdSortStockList.loc[0]))
# print((g_pdSortStockList.loc[0]))
# pdStock = g_pdSortStockList.loc[0]

def getStockTradeDate():
    datanow = datetime.datetime.today().date()
    if g_pdTraDay.empty:
        # print(datanow)
        if datanow.strftime("%w") == 0:
            datanow = datanow + datetime.timedelta(-2)
        else:
            datanow = datanow + datetime.timedelta(-1)
    else:
        while 1:
            strdate = datanow.strftime("%Y-%m-%d")
            # print(strdate)
            dataseries = g_pdTraDay.loc[g_pdTraDay['calendarDate'] == strdate]['isOpen']
            # print(dataseries)
            if dataseries.empty == False:
                if int(dataseries) == 1:
                    break
            datanow = datanow + datetime.timedelta(-1)
            
    datanow = datanow.strftime("%Y-%m-%d")
    print(datanow)
    return datanow
g_lastTraDate = getStockTradeDate()


def getStockToSql(pdStock, datanow, stockname):
    if(pd.isnull(pdStock['DATE'])):
        temp = "code=1%(code)06d&start=%(st)s&end=%(end)s"%{'code' : pdStock['SYMBOL'], 'st' : g_stockBeginDate.replace('-', ''), 'end' : datanow.replace('-', '')}
    else:
        temp = "code=1%(code)06d&start=%(st)s&end=%(end)s"%{'code' : pdStock['SYMBOL'], 'st' : str(pdStock['DATE']).replace('-', ''), 'end' : datanow.replace('-', '')}

    # if stockname == '002752昇兴股份' :
    #     temp = "code=1%(code)s&start=%(st)s&end=%(end)s"%{'code' : pdStock['SYMBOL'], 'st' : '20190101', 'end' : datanow.replace('-', '')}
    #     temp = ("http://quotes.money.163.com/service/chddata.html?" + temp +
    #             "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP")   
    # else:
    if pdStock['SYMBOL'] == '6':
        temp = temp.replace('code=1', 'code=0')
    temp = ("http://quotes.money.163.com/service/chddata.html?" + temp +
            "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP")              
    print(temp) 
    logfp.write("%(stockname)s get "%{'stockname' : stockname} + temp + '\n')
    logfp.flush()

    

    abs_dir = datapath + "\\%(stockname)s.csv"%{'stockname' : stockname}
    print(abs_dir)
    if (os.path.exists(abs_dir)):
        os.remove(abs_dir)
    socket.setdefaulttimeout(60)

#     getfinish = time.mktime(datetime.datetime.now().timetuple()) + 30
#     print(getfinish)
#     def getCsvCallback(blocknum, blocksize, totalsize):
#         nonlocal getfinish
#         per = 100.0 * blocknum * blocksize / totalsize
#         if per >= 100 :
#             getfinish = 0
# socket.setdefaulttimeout(30)
    # try:
    #     urllib.request.urlretrieve(temp, abs_dir)#, getCsvCallback) 
    # except socket.timeout:
    #     count = 1
    #     while count <= 5:
    #         try:
    #             urllib.request.urlretrieve(temp, abs_dir)#, getCsvCallback)                                              
    #             break
    #         except socket.timeout:
    #             err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
    #             print(err_info)
    #             count += 1
    #     if count > 5:
    #         print("download job failed!\n")
    #         g_pdSortStockList.loc[pdStock.name, 'DATE'] = None
            # pdStock.loc['DATE'] = None
    #         return pdStock
    # stockdata = pd.read_csv(abs_dir, encoding='gbk')


    try:
        stockdata = pd.read_csv(temp, encoding='gbk')#"gb2312")
    except socket.timeout:
        count = 1
        while count <= 5:
            try:
                stockdata = pd.read_csv(temp, encoding='gbk')#"gb2312")                                          
                break
            except socket.timeout:
                err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
                print(err_info)
                count += 1
            except urllib.error.URLError as e:
                if hasattr(e, 'code'):
                    print("e.code")
                    print(e.code)
                elif hasattr(e, 'reason'):
                    print("e.reason")
                    print(e.reason)
                logfp.write("urllib.error.URLError\n")
                logfp.flush()
                count = 10
        if count > 5:
            print("download job failed!\n")
            g_pdSortStockList.loc[pdStock.name, 'DATE'] = None
            pdStock.loc['DATE'] = None
            return pdStock

    # print(stockdata)
    # print(str(stockdata.index.size))
    if ( stockdata.empty == False):
        # stockname = stockdata.loc[0, '名称'].lower().replace('*', '_')
        # stocksymbol = stockdata.loc[0, '股票代码'][1:]
        # stockname = stocksymbol + stockname
        del stockdata['名称']
        del stockdata['前收盘']
        del stockdata['流通市值']
        del stockdata['股票代码']
        stockdata.rename(columns={'日期':'Date', '收盘价':'ClosePrise', '最高价':'HighPrise', '最低价':'LowPrise', '开盘价':'OpenPrise', 
                                '涨跌额':'UpDownPrice', '涨跌幅':'UpDownRange', '换手率':'TurnoverRate', 
                                '成交量':'Volume', '成交金额':'AMOUNT', '总市值':'MarketValue'},inplace=True) 
        # print(stockdata)
        if(pd.isnull(pdStock['DATE'])):
            stockdata.to_sql(stockname, con=engine, if_exists='replace', index=False) 
        else:
            stockdata.to_sql(stockname, con=engine, if_exists='append', index=False)  
        # pdStock['DATE'] = datanow
        g_pdSortStockList.loc[pdStock.name, 'DATE'] = datanow
        pdStock.loc['DATE'] = datanow
        logfp.write("update %(stock)s success\n"%{'stock' : stockname})
        logfp.flush() 
    else:
        # pdStock['DATE'] = None
        g_pdSortStockList.loc[pdStock.name, 'DATE'] = None
        pdStock.loc['DATE'] = None
        logfp.write("warning %(stock)s fail with none data\n"%{'stock' : stockname})
        logfp.flush() 

    if (os.path.exists(abs_dir)):
        os.remove(abs_dir)


def spider(pdStock):
    # print(type(pdStock))
    # print(pdStock['SYMBOL'])
    # nonlocal g_pdSortStockList
    # pdStock = slist.loc[item]
    stockname = str(pdStock['SYMBOL']) + str(pdStock['NAME'])
    # print("spider %(stock)s\n"%{'stock' : stockname})
    # pdStock['DATE'] = None #'2019-10-11'
    # datanow = datetime.datetime.now().strftime('%Y-%m-%d') 
    # if int(pdStock['VOLUME']) == 0:
    #     edatanow = 0
    # else:
    # temp = ("select `DATE` from `TABLE_NAME`  WHERE EXISTS  (select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA=\'%(db)s\' and TABLE_NAME=\'%(stock)s\')"%{'db' : g_dbName, 'stock' : stockname}
    #         )
    # print(temp)
    # data = pd.read_sql_query(temp, con = engine)
    edatanow = -1
    data = pd.read_sql_query("select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA=\'%(db)s\' and TABLE_NAME=\'%(stock)s\'"%{'db' : g_dbName, 'stock' : stockname},con = engine)
    # print(data)
    if ( data.empty == False):
        if int(pdStock['VOLUME']) == 0:
            edatanow = 0
        else:
            data = pd.read_sql_query("select  `DATE` from `%(stock)s` limit 1"%{'stock' : stockname},con = engine)
            # data = pd.read_sql_query("select `DATE` from `%(stock)s` where `%(stock)s`.DATE = \'%(date)s\'"%{'stock' : stockname, 'date' : g_lastTraDate},con = engine)
            # data = pd.read_sql_query("select `DATE` from `%(stock)s`"%{'stock' : stockname},con = engine)
            if ( data.empty == False):
                if(data.loc[0, 'DATE'] == g_lastTraDate):
                    edatanow = 0
                else:
                    if(pdStock['DATE'] == g_lastTraDate):
                        edatanow = 0
        
    # print(datanow +"---" + str(edatanow))
    if(edatanow):
        logfp.write("begin update %(symbol)s \n"%{'symbol':stockname})
        logfp.flush()
        getStockToSql(pdStock, g_lastTraDate, stockname)
    else:
        g_pdSortStockList.loc[pdStock.name, 'DATE'] = g_lastTraDate
        pdStock.loc['DATE'] = g_lastTraDate
    
    return pdStock


if __name__ == '__main__':   
    pool = ThreadPoolExecutor(max_workers=1)
    allitem = g_pdSortStockList.index.size-1
    nowitem = 0

    # def taskfortime(tasktime):
    #     while 1:
    #         if tasktime > time.time() + 60:
    #             break
    #         else:
    #             time.sleep(1)

    task_list = []
    # task_list.append(pool.submit(taskfortime, tasktime))
    for taskitem in range (allitem, -1, -1):
        # if g_pdSortStockList.loc[taskitem]['SYMBOL'][0] == '6':#6：沪A 9：沪B  3?0：深A 2:深B
        task_list.append(pool.submit(spider, g_pdSortStockList.loc[taskitem, {'SYMBOL', 'NAME', 'DATE', 'VOLUME'}]))
    # task_list = list(pool.map(spider,  g_pdSortStockList.loc[:, {'SYMBOL', 'NAME', 'DATE', 'VOLUME'}]))
    # wait(task_list, timeout=60, return_when=FIRST_COMPLETED)
    for f in as_completed(task_list):
        f_ret = f.result()
        nowitem += 1
        print("all\tnow\tpercent\ttime(s)")
        print("%(all)s\t%(now)s\t%(per).05s%%\t%(time)s"%{'all': allitem, 'now' : nowitem, 'per' : 100*nowitem/allitem, 'time' : (time.time()-begintime)})
        try:
            ret = f.done()
            if ret:
                if pd.isnull(f_ret['DATE']):
                    ret = "finish %(number)s%(name)s fail at %(time)s\n"%{'number' : f_ret['SYMBOL'], 'name' : f_ret['NAME'], 'time' : time.strftime("%H:%M:%S")}
                else:
                    ret = "finish %(number)s%(name)s done at %(time)s\n"%{'number' : f_ret['SYMBOL'], 'name' : f_ret['NAME'], 'time' : time.strftime("%H:%M:%S")}
                print(ret)
                logfp.write(ret)
                logfp.flush()
                # g_pdSortStockList
                # if (nowitem % 30 == 0):
                    # g_pdSortStockList.to_sql('000000amarket',con=engine, if_exists='replace', index=False) 
                g_pdSortStockList.to_csv(g_stockDataPath, index=False) 
            else:
                logfp.write(f)
                logfp.flush() 
        except Exception as e:
            f.cancel()
            ret = "finish %(number)s%(name)s error:%(err)s at %(time).02ss\n"%{'number' : f_ret['SYMBOL'], 'name' : f_ret['NAME'], 'err' : str(e), 'time' : time.strftime("%H:%M:%S")}
            print(ret)
            logfp.write(ret)
            logfp.flush() 
        # if  f_ret['SYMBOL'] == g_pdSortStockList.loc[1]['SYMBOL']:
        # if  f_ret['SYMBOL'] == g_pdSortStockList.loc[g_pdSortStockList.index.size - 1]['SYMBOL']:
# g_pdSortStockList.to_sql('000000amarket',con=engine, if_exists='replace', index=False)  
g_pdSortStockList.to_csv(g_stockDataPath, index=False) 
logfp.write("A market get data program end at %(time)s use %(use).02ss\n"%{'time' : time.strftime("%H:%M:%S"), 'use' :(time.time()-begintime)})
logfp.flush()
pd.set_option('display.max_rows',None)#max_colwidth
print(g_pdSortStockList[ g_pdSortStockList[ 'DATE'].isnull() ])
logfp.write("%(symbol)s \n"%{'symbol':g_pdSortStockList[ g_pdSortStockList[ 'DATE'].isnull() ]})
logfp.flush()
pd.set_option('display.max_rows',10 )
logfp.close()
# engine.
