# -*- coding: utf-8 -*-
import sys
from Ui_mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal , Qt #for qt signal custom

class LogicWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    signal_Show = pyqtSignal(str)
    signal_Close = pyqtSignal(int, str)

    def __init__(self, parent=None):
        super(LogicWindow, self).__init__(parent)
        self.setupUi(self)
        # test menu signandslot connect 
        self.menu_Test.triggered[QtWidgets.QAction].connect(self.menuTestFunction)
        self.signal_Show.connect(self.testShowFunction)
        self.signal_Close.connect(self.testCloseFunction)
        
        # file menu signandslot connect 
        self.action_New.triggered.connect(self.actionNewFunction)
        self.action_Open.triggered['bool'].connect(self.actionOpenFunction)
        self.action_Save.triggered['bool'].connect(self.actionSaveFunction)
        self.action_Quit.triggered['bool'].connect(self.actionQuitFunction)

    def showEvent(self, evt):
        print("this is show"  )
        
    def closeEvent(self, evt):
        print("this is close"  )

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
        

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    logicWindow = LogicWindow()
    logicWindow.show()
    sys.exit(app.exec_())
