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


class GraphWork(QObject):
    signal_Update =pyqtSignal(int, int, str)
    signal_Show =pyqtSignal(str, str)
    signal_UnShow =pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(GraphWork, self).__init__(parent)
        self.lastcode = ''

    def graphInitWorker(self, fig, codename='000001平安银行'):
        self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        self.graphUpdate(codename)
        self.graphShow(codename)
        
    def graphUpdate(self, codename):
        if self.lastcode != codename:
            self.stockdata = stock_GetLocalData(codename)
            if self.stockdata.empty:
                self.lastcode = ''
            else:
                self.lastcode = codename
                tdata = pd.DataFrame(np.arange(0,len(self.stockdata)))
                pricearray = pd.concat([tdata, self.stockdata[['开盘价', '最高价', '最低价', '收盘价']]],axis=1)
                self.datepricelist =np.array(pricearray).tolist()
                print(self.datepricelist)
    
    def graphShow(self, codename, day=60, space=1, needstr='all'):
        if needstr == 'all':
            mpf.candlestick_ohlc(self.axes, self.datepricelist[-day: -space :], width=1.2, colorup='r', colordown='green')
            self.axes.plot(self.stockdata.index[-day: -space :], self.stockdata['前收盘'][-day: -space :], color='magenta')
            self.axes.plot(self.stockdata.index[-day: -space :], self.stockdata['开盘价'][-day: -space :], color='red')
            self.axes.plot(self.stockdata.index[-day: -space :], self.stockdata['最高价'][-day: -space :], color='blue')
            self.axes.plot(self.stockdata.index[-day: -space :], self.stockdata['最低价'][-day: -space :], color='yellow')
            self.axes.plot(self.stockdata.index[-day: -space :], self.stockdata['收盘价'][-day: -space :], color='green')
        elif needstr == 'candle_show':
            mpf.candlestick_ohlc(self.axes, self.datepricelist[-day: -space :], width=1.2, colorup='r', colordown='green')
        elif needstr == 'candle_close':
            mpf.candlestick_ohlc(self.axes, self.datepricelist[-day: -space :], width=1.2, colorup='r', colordown='green')
        elif needstr == 'before_show':
            self.axes.plot(self.stockdata.index[-day: -space :], self.stockdata['前收盘'][-day: -space :], color='magenta')
        elif needstr == 'before_close':
            self.axes.plot(self.stockdata.index[-day: -space :], self.stockdata['前收盘'][-day: -space :], color='magenta')

# 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键
class StockGraph(FigureCanvas):
    
    def __init__(self, parent=None, width=11, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        FigureCanvas.__init__(self, fig) # 初始化父类
        fig.subplots_adjust(bottom=0.2)
        self.setParent(parent)
        

        self.GraphThread=QThread()
        self.GraphWorker=GraphWork()
        self.GraphWorker.moveToThread(self.GraphThread)
        # self.GraphThread.started.connect(self.GraphWorker.graphInitWorker)
        # self.GraphWorker.signal_Add.connect(self.treeItemAdd)
        self.GraphThread.start()
        self.GraphWorker.graphInitWorker(fig)
        
    def paintStockPrice(self, codename):
        pass


