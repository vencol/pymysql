# -*- coding: utf-8 -*-
import sys
import time
from Ui_mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QTreeWidgetItem, QCompleter#, QBrush, QColor
from PyQt5.QtCore import pyqtSignal, QDate, QStringListModel, QThread, QObject

import numpy as np
import pandas as pd
from StockCode import *

import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])

# http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQA%3BEXCHANGE%3ACNSESH&fields=SYMBOL&count=5000&type=query
class WorkObject(QObject):
    signal_Quit =pyqtSignal()

    def __init__(self,parent=None):
        super(WorkObject, self).__init__(parent)
        self.startType = 0

    def mainWorker(self):
        if self.startType == 0:
            time.sleep(0.1)
        
    def addTreeData(self, chunk, treeWidget):      
        codename = "%(code)06d"%{'code':chunk.loc['SYMBOL']}
        tlist=[stock_CodeIdentify(codename), codename, chunk.loc['NAME']]
        codename = tlist[1] + tlist[2]
        if tlist[0] == '':
            print(tlist)
        elif tlist[0] == MARKER_TYPE_SZ_ZXB:
            UpParent = treeWidget.topLevelItem(2)
            child = QTreeWidgetItem(UpParent)
            child.setText(0, codename)
        elif tlist[0] == MARKER_TYPE_SH_KCB:
            UpParent = treeWidget.topLevelItem(3)
            child = QTreeWidgetItem(UpParent)
            child.setText(0, codename)
        elif tlist[0] == MARKER_TYPE_SZ_CYB:
            UpParent = treeWidget.topLevelItem(4)
            child = QTreeWidgetItem(UpParent)
            child.setText(0, codename)
        elif MARKER_TYPE_B in tlist[0]:
            if tlist[0] == MARKER_TYPE_SZ_B:
                UpParent = treeWidget.topLevelItem(1).child(0)
                child = QTreeWidgetItem(UpParent)
                child.setText(0, codename)
            elif tlist[0] == MARKER_TYPE_SH_B:
                UpParent = treeWidget.topLevelItem(1).child(1)
                child = QTreeWidgetItem(UpParent)
                child.setText(0, codename)
        elif MARKER_TYPE_A in tlist[0]:
            if tlist[0] == MARKER_TYPE_SZ_A:
                UpParent = treeWidget.topLevelItem(0).child(0)
                child = QTreeWidgetItem(UpParent)
                child.setText(0, codename)
            elif tlist[0] == MARKER_TYPE_SH_A:
                UpParent = treeWidget.topLevelItem(0).child(1)
                child = QTreeWidgetItem(UpParent)
                child.setText(0, codename)

    def treeInitWEork(self, listdata):
        print("this is listdata"  )
        AllStockData = listdata[0]
        for i in range(0, len(AllStockData)):
            chunk = AllStockData.loc[i]
            self.addTreeData(chunk, listdata[1])

        self.signal_Quit.emit( )		

class LogicWindow(QMainWindow, Ui_MainWindow):
    signal_Show = pyqtSignal(str)
    signal_Close = pyqtSignal(int, str)

    signal_StartTreeInitWEork = pyqtSignal(list)

    
    g_datapath = os.path.dirname(os.path.abspath(__file__))
    logpath = g_datapath + '\\uidebug.txt'
    logfp = open(logpath, "w")
    logfp.write("start the A market get data program at s\n")

    def __init__(self, parent=None):
        super(LogicWindow, self).__init__(parent)
        self.setupUi(self)
        self.setMenuData()
        self.setInitData()
        self.setTreeData()


    def showEvent(self, evt):
        print("this is show"  )
        
    def closeEvent(self, evt):
        print("this is close"  )

     
    def setMenuData(self):   
        # test menu signandslot connect 
        self.menu_Test.triggered[QAction].connect(self.menuTestFunction)
        self.signal_Show.connect(self.testShowFunction)
        self.signal_Close.connect(self.testCloseFunction)        
        # file menu signandslot connect 
        self.action_New.triggered.connect(self.actionNewFunction)
        self.action_Open.triggered['bool'].connect(self.actionOpenFunction)
        self.action_Save.triggered['bool'].connect(self.actionSaveFunction)
        self.action_Quit.triggered['bool'].connect(self.actionQuitFunction)

    # menu slot function
    def actionNewFunction(self):
        print("this is new" )

    def actionOpenFunction(self):
        print("this is open" )

    def actionSaveFunction(self):
        print("this is save" )

    def actionQuitFunction(self):
        print("this is quit" )
        self.close()

    # test slot function
    def menuTestFunction(self, ob):
        self.statusBar().showMessage("this is menu" + ob.text() )
        # print("this is menu" + ob.text() )
        if ob == self.action_Show_test:
            self.signal_Show.emit("show here")
        elif ob == self.action_Close_test:
            self.signal_Close.emit(4, "close here")
        else:
            print("show o=n again")

    def testShowFunction(self, message):
        print("emit a message for " + message)

    def testCloseFunction(self, intstr, test):
        print("emit a message 1 for " + test)
        print("emit a message 2 for " + str(intstr) + test)


    def setInitData(self):
        # self.AllStockData = pd.DataFrame()
        self.dateEdit_Start.setDate(QDate.currentDate())
        self.dateEdit_End.setDate(QDate.currentDate())
        # self.lineEdit_StockCode.editingFinished.connect(self.editCodeFinished)
        self.lineEdit_StockCode.textChanged['QString'].connect(self.searchCodeChange)
        # self.lineEdit_StockName.editingFinished.connect(self.editCodeFinished)
        # self.lineEdit_StockName.textChanged['QString'].connect(self.searchNameChange)
        self.setCompleter()

    def setCompleter(self):#use more time
        self.completerCodeEdit = QCompleter()
        # # 设置匹配模式  有三种： Qt.MatchStartsWith 开头匹配（默认）  Qt.MatchContains 内容匹配  Qt.MatchEndsWith 结尾匹配
        self.completerCodeEdit.setFilterMode(QtCore.Qt.MatchContains)
        # # 设置补全模式  有三种： QCompleter.PopupCompletion（默认）  QCompleter.InlineCompletion   QCompleter.UnfilteredPopupCompletion
        # self.completerCodeEdit.setCompletionMode(QCompleter.PopupCompletion)
        self.completerCodeListModel = QStringListModel()
        self.lineEdit_StockCode.setCompleter(self.completerCodeEdit)
        self.completerCodeEdit.setModel(self.completerCodeListModel)
        self.completerCodeEdit.activated['QString'].connect(self.completerCodeFunction)

    def completerCodeFunction(self, text):
        if len(text) >= 6:
            items = self.treeWidget.findItems(text, QtCore.Qt.MatchStartsWith  | QtCore.Qt.MatchRecursive)
            # self.treeWidget.collapseItem(self.treeWidget.topLevelItem(0))
            # self.treeWidget.expandItem(self.treeWidget.topLevelItem(0))
            self.treeWidget.collapseAll()
            self.treeWidget.setCurrentItem(items[0])

    def searchCodeChange(self, text):
        if text == '' or len(text) >= 6:
            pass
        else:
            if text.isdigit():
                items = self.treeWidget.findItems(text, QtCore.Qt.MatchStartsWith  | QtCore.Qt.MatchRecursive)
                itlen = len(items)
                if itlen == 0:
                    items = self.treeWidget.findItems(text, QtCore.Qt.MatchContains  | QtCore.Qt.MatchRecursive)
            else:
                items = self.treeWidget.findItems(text, QtCore.Qt.MatchContains  | QtCore.Qt.MatchRecursive)
            itlen = len(items)
            if itlen:
                setlist = []
                if itlen > 7:
                    itlen = 7
                for i in range(0, itlen):
                    setlist.append(items[i].text(0))
                # print(setlist)
                self.completerCodeListModel.setStringList(setlist)


    def setTreeData(self):#use more source
        self.treeWidget.headerItem().setText(0, "股市")
        UpParent = QTreeWidgetItem(self.treeWidget)
        UpParent.setText(0, "A股")
        child = QTreeWidgetItem(UpParent)
        child.setText(0, "深市A股")
        child = QTreeWidgetItem(UpParent)
        child.setText(0, "沪市A股")
        UpParent = QTreeWidgetItem(self.treeWidget)
        UpParent.setText(0, "B股")
        child = QTreeWidgetItem(UpParent)
        child.setText(0, "深市B股")
        child = QTreeWidgetItem(UpParent)
        child.setText(0, "沪市B股")
        UpParent = QTreeWidgetItem(self.treeWidget)
        UpParent.setText(0, "中小板")
        UpParent = QTreeWidgetItem(self.treeWidget)
        UpParent.setText(0, "科创板")
        UpParent = QTreeWidgetItem(self.treeWidget)
        UpParent.setText(0, "创业板")
        self.treeWidget.itemClicked['QTreeWidgetItem*','int'].connect(self.treeItemClick)
        
        self.AllStockData = stock_IdentifyType(1)
        datalist=[]
        datalist.append(self.AllStockData)
        datalist.append(self.treeWidget)
        self.WorkThread=QThread()
        self.Worker=WorkObject()
        self.Worker.moveToThread(self.WorkThread)
        self.WorkThread.started.connect(self.Worker.mainWorker)
        self.signal_StartTreeInitWEork.connect(self.Worker.treeInitWEork)
        self.Worker.signal_Quit.connect(self.WorkQuit)
        self.WorkThread.start()
        self.signal_StartTreeInitWEork.emit(datalist)

    def WorkQuit(self,):
        self.WorkThread.quit()


    def treeItemClick(self,item,n):
        print("this is item : " + item.text(n) + "num is : " + str(n))
        self.lineEdit_StockCode.setText(item.text(n))

        

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    logicWindow = LogicWindow()
    logicWindow.show()
    sys.exit(app.exec_())