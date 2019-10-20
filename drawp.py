# -*-coding:utf8-*-


import os
import time
import datetime 

# import matplotlib.pyplot as plt
# from pylab import rcParams

import numpy as np
import pandas as pd
import pyqtgraph as pg

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor, as_completed, wait, ALL_COMPLETED,FIRST_COMPLETED


# config data
g_needUpdateMarket  = 0
g_stockBeginDate    = '2008-01-01'
g_stockOpenDatePath = '\\.tradday.csv'    
g_dbName            = 'bstock'
g_itChunkSize  = 50
g_itChunkList = []


# 在Windows下经常用python open函数的人相信都遇到过UnicodeDecodeError: ‘gbk’ codec…这种编码问题。而且很多有经验的人应该知道解决方法是加上参数encoding=“utf-8”，因为"utf-8"是更通用的编码：
import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])

# logfileimport _locale
g_datapath = os.path.dirname(os.path.abspath(__file__))
logpath = g_datapath + '\\000001drawp_log.txt'
print(logpath)
logfp = open(logpath, "w")
logfp.write("start the A market get data program at %(time)s\n"%{'time' : time.strftime("%H:%M:%S")})
begintime = time.time()



def getStockData(csvname):
    if csvname.strip() == '':
        return None
    else:
        csvpath = g_datapath + '\\acsvdata\\' + csvname + '.csv'
        if (os.path.exists(csvpath) == False):
            return None
        else:
            csvStockData = pd.read_csv(csvpath, encoding='gbk')#, iterator=True)
            # del csvStockData['名称']
            # del csvStockData['前收盘']
            # del csvStockData['流通市值']
            # del csvStockData['股票代码']
            csvStockData = csvStockData.drop(['名称', '前收盘', '流通市值', '股票代码'], axis = 1)
            csvStockData.rename(columns={'日期':'Date', '收盘价':'ClosePrise', '最高价':'HighPrise', '最低价':'LowPrise', '开盘价':'OpenPrise', 
                                    '涨跌额':'UpDownPrice', '涨跌幅':'UpDownRange', '换手率':'TurnoverRate', 
                                '成交量':'Volume', '成交金额':'AMOUNT', '总市值':'MarketValue'},inplace=True) 
            # print(csvStockData)
            # csvStockData = csvStockData.set_index(pd.to_datetime(csvStockData['Date']))
            # print(csvStockData)
            return csvStockData

        
def drawStockData(num, name, type=0, is_show=1, output=None):
    stockname = "%(num)06s%(name)s"%{'num' : num, 'name' : name}
    drawStockData = getStockData(stockname)

    # pg.plot.figure()
    pg.plot(drawStockData["Date"], drawStockData["OpenPrise"], 'r-', label="OpenPrise")
    pg.plot(drawStockData["Date"], drawStockData["ClosePrise"], 'g-', label="ClosePrise")#, 'bo'
    pg.QtGui.QGuiApplication.exec_()
    # pg.grid(ls='--')
    # pg.legend()
    # pg.xlabel('date')
    # pg.ylabel('value')
    # pg.legend()
    # pg.xticks(rotation=90)

    # rcParams['figure.figsize'] = 18, 50
    # plt.figure()

    # # 收盘价
    # plt.subplot(2, 1, 1)
    # plt.plot(drawStockData["Date"], drawStockData["OpenPrise"], 'r-', label="OpenPrise")
    # plt.plot(drawStockData["Date"], drawStockData["ClosePrise"], 'g-', label="ClosePrise")#, 'bo'
    # plt.grid(ls='--')
    # plt.legend()
    # plt.subplot(2, 1, 2)
    # plt.plot(drawStockData["Date"], drawStockData["HighPrise"], 'b-', label="HighPrise")
    # plt.plot(drawStockData["Date"], drawStockData["LowPrise"], 'y-', label="LowPrise")
    # plt.grid(ls='--')
    # # plt.plot(drawStockData["Date"], drawStockData["Volume"], label="Volume")
    # # plt.plot(drawStockData["Date"], drawStockData["AMOUNT"], label="AMOUNT")
    # plt.xlabel('date')
    # plt.ylabel('value')
    # plt.legend()
    # plt.xticks(rotation=90)

    # plt.tight_layout()
    # if is_show:
    #     plt.show()
    # if output is not None:
    #     plt.savefig(output)

def task_loop():
    pool = ThreadPoolExecutor(max_workers=1)
    allitem = 10
    nowitem = 0
    task_list = []
    # task_list.append(pool.submit(taskfortime, tasktime))
    # for taskitem in range (0, allitem, 1):
    for taskitem in range (allitem, -1, -1):
        # if g_pdSortStockList.loc[taskitem]['SYMBOL'][0] == '6':#6：沪A 9：沪B  3?0：深A 2:深B
        task_list.append(pool.submit(drawStockData, taskitem))
        # task_list.append(pool.submit(spider, g_pdSortStockList.loc[taskitem, {'SYMBOL', 'NAME', 'DATE', 'VOLUME'}]))
    # wait(task_list, timeout=60, return_when=FIRST_COMPLETED)
    for f in as_completed(task_list):
        f_ret = f.result()
        nowitem += 1
        print("all\tnow\tpercent\ttime(s)")
        print("%(all)s\t%(now)s\t%(per).05s%%\t%(time).05ss"%{'all': allitem, 'now' : nowitem, 'per' : 100*nowitem/allitem, 'time' : (time.time()-begintime)})
        
        logfp.write("%(all)s\t%(now)s\t%(per).05s%%\t%(time).05ss"%{'all': allitem, 'now' : nowitem, 'per' : 100*nowitem/allitem, 'time' : (time.time()-begintime)})
        logfp.flush() 
        try:
            ret = f.done()
            if ret:
                if pd.isnull(f_ret['DATE']):
                    ret = "finish %(number)s%(name)s fail at %(time)s use %(use).05ss\n"%{'number' : f_ret['SYMBOL'], 'name' : f_ret['NAME'], 'time' : time.strftime("%H:%M:%S"), 'use' : (time.time()-begintime)}
                else:
                    ret = "finish %(number)s%(name)s done at %(time)s use %(use).05ss %(data)s\n"%{'number' : f_ret['SYMBOL'], 'name' : f_ret['NAME'], 'time' : time.strftime("%H:%M:%S"), 'use' : (time.time()-begintime), 'data':f_ret['DATE']}
                print(ret)
                logfp.write(ret)
                logfp.flush()
            else:
                logfp.write(f)
                logfp.flush() 
        except Exception as e:
            f.cancel()
            ret = "finish %(number)s%(name)s error:%(err)s at %(time).05ss\n"%{'number' : f_ret['SYMBOL'], 'name' : f_ret['NAME'], 'err' : str(e), 'time' : time.strftime("%H:%M:%S")}
            print(ret)
            logfp.write(ret)
            logfp.flush() 


if __name__ == '__main__':   
    # taskloop = 0
    # while( g_pdSortStockList[ 'DATE'].isnull().empty == False ):
    # task_loop()
        # taskloop += 1
        # if taskloop >= 3:
        #     break
    drawStockData('002966', '苏州银行')
            
logfp.write("A market get data program end at %(time)s use %(use).05ss\n"%{'time' : time.strftime("%H:%M:%S"), 'use' :(time.time()-begintime)})
logfp.flush()
pd.set_option('display.max_rows',None)#max_colwidth
# print(g_pdSortStockList[ g_pdSortStockList[ 'DATE'].isnull() ])
# logfp.write("%(symbol)s \n"%{'symbol':g_pdSortStockList[ g_pdSortStockList[ 'DATE'].isnull() ]})
logfp.flush()
pd.set_option('display.max_rows',10 )
logfp.close()
# sys.exit()
os._exit(1)
# engine.
