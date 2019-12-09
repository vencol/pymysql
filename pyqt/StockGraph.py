# -*- coding: utf-8 -*-
import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])


import numpy as np
from StockCode import *
from PyQt5.QtCore import pyqtSignal, QThread, QObject

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import mpl_finance as mpf

# 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键
class StockGraph(FigureCanvas):
    
    def __init__(self, parent=None, width=11, height=5, dpi=100):
        # self.GraphThread=QThread()
        fig = Figure(figsize=(width, height), dpi=dpi)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        FigureCanvas.__init__(self, fig) # 初始化父类
        fig.subplots_adjust(bottom=0.2)
        self.setParent(parent)
        self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

    def test(self):
        x = [1,2,3,4,5,6,7,8,9]
        y = [23,21,32,13,3,132,13,3,1]
        self.axes.plot(x, y)
        
    def paintStockPrice(self, codename):
        stockdata = stock_GetLocalData(codename)
        # print(stockdata)
        # print(stockdata[['日期', '开盘价', '最高价', '最低价', '收盘价']])
        # stockdata['日期'] = pd.to_datetime(stockdata['日期'])
        # stockdata.set_index("日期", inplace=True)
        # print(stockdata)
        # stockdata[['开盘价', '最高价', '最低价', '收盘价']].plot(figsize=(self.width, self.height))
        # print(stockdata.axes[0])
        
        self.axes.plot(stockdata.index[-60:], stockdata['前收盘'][-60:], color='magenta')
        self.axes.plot(stockdata.index[-60:], stockdata['开盘价'][-60:], color='red')
        self.axes.plot(stockdata.index[-60:], stockdata['最高价'][-60:], color='blue')
        self.axes.plot(stockdata.index[-60:], stockdata['最低价'][-60:], color='yellow')
        self.axes.plot(stockdata.index[-60:], stockdata['收盘价'][-60:], color='green')

        # tarray =np.array(stockdata.index)
        tdata = pd.DataFrame(np.arange(0,len(stockdata)))
        print(tdata)
        pricearray = pd.concat([tdata, stockdata[['开盘价', '最高价', '最低价', '收盘价']]],axis=1)
        print(pricearray)
        datepricelist =np.array(pricearray).tolist()
        # pricearray =np.array(stockdata[['开盘价', '最高价', '最低价', '收盘价']])
        # pricelist = (tarray + pricearray).tolist()
        # print(type(pricelist))
        # print(pricelist)
        # tlist = list(range(len(stockdata)))
        # print(tlist)
        # datepricelist = [tlist, pricelist]
        # print(sum(datepricelist, []))
        mpf.candlestick_ohlc(self.axes, datepricelist[-60:], width=1.2, colorup='r', colordown='green')
        # data_list = []
        # for row in stockdata[['日期', '开盘价', '最高价', '最低价', '收盘价']]:
        #     print(row)
        #     dates,open,high,low,close = row[:]
        #     # 将时间转换为数字
        #     # date_time = datetime.datetime.strptime(dates,'%Y-%m-%d')
        #     # t = date2num(date_time)
        #     datas = (dates,open,high,low,close)
        #     print(datas)
        #     data_list.append(datas)
        # if stockdata:
        #     self.axes.xaxis_date()#X轴为日期
        #     plt.xticks(rotation=45)#斜45°
        #     plt.title("股票代码：601558两年K线图")
        #     plt.xlabel("时间")
        #     plt.ylabel("股价（元）")
        #     # mpf.candlestick_ohlc(self.axes,quotes,width=1.2,colorup='r',colordown='green')
        #     plt.grid(True)


class GraphWork(QObject):
    signal_Update =pyqtSignal(int, int, str)

    def __init__(self,parent=None):
        super(GraphWork, self).__init__(parent)
        self.startType = 0

    def graphInitWorker(self):
        pass
