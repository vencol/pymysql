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
        self.LastCode = ''
        self.BeforeLine = 0
        self.LowLine = 0
        self.HighLine = 0
        self.OpenLine = 0
        self.CloseLine = 0

    def graphInitWorker(self, fig, codename='000001平安银行'):
        self.Axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        self.graphShowParam(codename)
        self.graphShowCandle(1)
        # self.graphShowCandle(0)
        
    def graphShowParam(self, codename, periodday=60, periodspace=1):
        if self.LastCode != codename:
            self.StockData = stock_GetLocalData(codename)
            if self.StockData.empty:
                self.LastCode = ''
            else:
                self.LastCode = codename
                self.PeriodDay = periodday
                self.PeriodSpace = periodspace
                tdata = pd.DataFrame(np.arange(0,len(self.StockData)))
                pricearray = pd.concat([tdata, self.StockData[['开盘价', '最高价', '最低价', '收盘价']]],axis=1)
                self.DatepPiceList =np.array(pricearray).tolist()
                print(self.DatepPiceList)
    
    def graphShowCandle(self, show):
        if self.LastCode and self.PeriodDay <= len(self.StockData):
            if show:
                self.BeforeLine = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['前收盘'][-self.PeriodDay: -self.PeriodSpace :], color='magenta')
            elif self.BeforeLine:
                self.BeforeLine.pop(0).remove()
        # if self.LastCode and self.PeriodDay <= len(self.StockData):
        #     if show:
        #         self.CandleLine = mpf.candlestick_ohlc(self.Axes, self.DatepPiceList[-self.PeriodDay: -self.PeriodSpace :], width=1.2, colorup='r', colordown='green')
        #     elif self.CandleLine:
        #         self.CandleLine.remove()
        # if needstr == 'all':
        #     self.BeforeLine = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['前收盘'][-self.PeriodDay: -self.PeriodSpace :], color='magenta')
        #     self.OpenLine   = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['开盘价'][-self.PeriodDay: -self.PeriodSpace :], color='red')
        #     self.HighLine   = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['最高价'][-self.PeriodDay: -self.PeriodSpace :], color='blue')
        #     self.LowLine    = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['最低价'][-self.PeriodDay: -self.PeriodSpace :], color='yellow')
        #     self.CloseLine  = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['收盘价'][-self.PeriodDay: -self.PeriodSpace :], color='green')
        # elif needstr == 'candle_show':
        #     mpf.candlestick_ohlc(self.Axes, self.DatepPiceList[-self.PeriodDay: -self.PeriodSpace :], width=1.2, colorup='r', colordown='green')
        # elif needstr == 'candle_close':
        #     mpf.candlestick_ohlc(self.Axes, self.DatepPiceList[-self.PeriodDay: -self.PeriodSpace :], width=1.2, colorup='r', colordown='green')
        # elif needstr == 'before_show':
        #     self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['前收盘'][-self.PeriodDay: -self.PeriodSpace :], color='magenta')
        # elif needstr == 'before_close':
        #     self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['前收盘'][-self.PeriodDay: -self.PeriodSpace :], color='magenta')

# 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键
class StockGraph(FigureCanvas):
    
    def __init__(self, parent=None, width=11, height=5, dpi=100):
        # super(StockGraph, self).__init__(parent)
        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        FigureCanvas.__init__(self, self.fig) # 初始化父类
        self.fig.subplots_adjust(bottom=0.2)
        self.setParent(parent)

        self.LastCode = ''
        self.BeforeLine = 0
        self.LowLine = 0
        self.HighLine = 0
        self.OpenLine = 0
        self.CloseLine = 0
        

        # self.GraphThread=QThread()
        # self.GraphWorker=GraphWork()
        # self.GraphWorker.moveToThread(self.GraphThread)
        # # self.GraphThread.started.connect(self.GraphWorker.graphInitWorker)
        # # self.GraphWorker.signal_Add.connect(self.treeItemAdd)
        # self.GraphThread.start()
        # self.GraphWorker.graphInitWorker(fig)
        
    def paintStockPrice(self, codename):
        pass

    def graphInitPriceWorker(self, codename='000001平安银行'):
        self.Axes = self.fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        self.graphShowParam(codename)
        self.graphShowBeforeLine(1)
        self.graphShowOpenLine(1)
        self.graphShowCloseLine(1)
        self.graphShowHighLine(1)
        self.graphShowLowLine(1)
        
    def graphShowParam(self, codename, periodday=60, periodspace=1):
        if self.LastCode != codename:
            self.StockData = stock_GetLocalData(codename)
            if self.StockData.empty:
                self.LastCode = ''
            else:
                self.LastCode = codename
                self.PeriodDay = periodday
                self.PeriodSpace = periodspace
                tdata = pd.DataFrame(np.arange(0,len(self.StockData)))
                pricearray = pd.concat([tdata, self.StockData[['开盘价', '最高价', '最低价', '收盘价']]],axis=1)
                self.DatepPiceList =np.array(pricearray).tolist()
                # print(self.DatepPiceList)
    
    def graphShowBeforeLine(self, show):
        if self.LastCode and self.PeriodDay <= len(self.StockData):
            if show:
                self.BeforeLine = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['前收盘'][-self.PeriodDay: -self.PeriodSpace :], color='magenta')
            elif self.BeforeLine:
                self.BeforeLine.pop(0).remove()
    
    def graphShowOpenLine(self, show):
        if self.LastCode and self.PeriodDay <= len(self.StockData):
            if show:
                self.OpenLine = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['开盘价'][-self.PeriodDay: -self.PeriodSpace :], color='red')
            elif self.OpenLine:
                self.OpenLine.pop(0).remove()
    
    def graphShowCloseLine(self, show):
        if self.LastCode and self.PeriodDay <= len(self.StockData):
            if show:
                self.CloseLine = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['收盘价'][-self.PeriodDay: -self.PeriodSpace :], color='green')
            elif self.CloseLine:
                self.CloseLine.pop(0).remove()
    
    def graphShowHighLine(self, show):
        if self.LastCode and self.PeriodDay <= len(self.StockData):
            if show:
                self.HighLine = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['最高价'][-self.PeriodDay: -self.PeriodSpace :], color='blue')
            elif self.HighLine:
                self.HighLine.pop(0).remove()
    
    def graphShowLowLine(self, show):
        if self.LastCode and self.PeriodDay <= len(self.StockData):
            if show:
                self.LowLine = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['最低价'][-self.PeriodDay: -self.PeriodSpace :], color='yellow')
            elif self.LowLine:
                self.LowLine.pop(0).remove()

