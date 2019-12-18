# -*- coding: utf-8 -*-
import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])


import numpy as np
from StockCode import *
from PyQt5.QtCore import pyqtSignal, QThread, QObject
from PyQt5.QtWidgets import QSizePolicy

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
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding,  QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

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
                tdata = pd.DataFrame(np.arange(0,len(self.StockData)))
                pricearray = pd.concat([tdata, self.StockData[['开盘价', '最高价', '最低价', '收盘价']]],axis=1)
                self.DatepPiceList =np.array(pricearray).tolist()
                # print(self.DatepPiceList)
        if self.StockData.empty :
            self.PeriodSpace = periodspace
            if periodday * periodspace > len(self.StockData):
                self.PeriodDay = len(self.StockData) / 3
            else:
                self.PeriodDay = periodday
        else:
            self.PeriodDay = 50000
        
    
    def graphShowBeforeLine(self, show):
        if self.LastCode and self.PeriodDay <= len(self.StockData):
            if show:
                if self.BeforeLine:
                    self.BeforeLine[0].set_color('magenta')
                else:
                    self.BeforeLine = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['前收盘'][-self.PeriodDay: -self.PeriodSpace :], color='magenta')
            elif self.BeforeLine:
                self.BeforeLine[0].set_color('white')
                # self.BeforeLine.pop(0).remove()
            self.draw()
    
    def graphShowOpenLine(self, show):
        if self.LastCode and self.PeriodDay <= len(self.StockData):
            if show:
                if self.OpenLine:
                    self.OpenLine[0].set_color('red')
                else:
                    self.OpenLine = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['开盘价'][-self.PeriodDay: -self.PeriodSpace :], color='red')
            elif self.OpenLine:
                self.OpenLine[0].set_color('white')
                # self.OpenLine.pop(0).remove()
            self.draw()
    
    def graphShowCloseLine(self, show):
        if self.LastCode and self.PeriodDay <= len(self.StockData):
            if show:
                if self.CloseLine:
                    self.CloseLine[0].set_color('green')
                else:
                    self.CloseLine = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['收盘价'][-self.PeriodDay: -self.PeriodSpace :], color='green')
            elif self.CloseLine:
                self.CloseLine[0].set_color('white')
                # self.CloseLine.pop(0).remove()
            self.draw()
    
    def graphShowHighLine(self, show):
        if self.LastCode and self.PeriodDay <= len(self.StockData):
            if show:
                if self.HighLine:
                    self.HighLine[0].set_color('blue')
                else:
                    self.HighLine = self.Axes.plot(self.StockData.index[-self.PeriodDay: -self.PeriodSpace :], self.StockData['最高价'][-self.PeriodDay: -self.PeriodSpace :], color='blue')
            elif self.HighLine:
                self.HighLine[0].set_color('white')
            self.draw()
    
    def graphShowLowLine(self, show):
        if self.LastCode and self.PeriodDay <= len(self.StockData):
            if show:
                if self.LowLine:
                    self.LowLine[0].set_color('yellow')
                else:# 没有判断时间是因为设置参数判断了
                    MaxDay = self.PeriodDay * self.PeriodSpace
                    CellData = self.StockData['最低价'][-MaxDay : : self.PeriodSpace]
                    CellData.index = range(0, self.PeriodDay)
                    DrawData = CellData
                    for i in range(1 , self.PeriodSpace):
                        CellData = self.StockData['最低价'][-MaxDay + i : : self.PeriodSpace]
                        CellData.index = range(0, self.PeriodDay)
                        DrawData = DrawData + CellData
                    DrawData = DrawData / self.PeriodSpace
                    print(DrawData)
                    self.LowLine = self.Axes.plot(self.StockData.index[-MaxDay + self.PeriodSpace - 1 : : self.PeriodSpace], DrawData, color='yellow')
            elif self.LowLine:
                self.LowLine[0].set_color('white')
                # self.LowLine.pop(0).remove()
            self.draw()

