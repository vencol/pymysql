# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\study\python\pymysql\pyqt\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 809)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_StockCode = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_StockCode.sizePolicy().hasHeightForWidth())
        self.label_StockCode.setSizePolicy(sizePolicy)
        self.label_StockCode.setObjectName("label_StockCode")
        self.horizontalLayout_3.addWidget(self.label_StockCode)
        self.lineEdit_StockCode = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_StockCode.sizePolicy().hasHeightForWidth())
        self.lineEdit_StockCode.setSizePolicy(sizePolicy)
        self.lineEdit_StockCode.setMinimumSize(QtCore.QSize(130, 0))
        self.lineEdit_StockCode.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit_StockCode.setObjectName("lineEdit_StockCode")
        self.horizontalLayout_3.addWidget(self.lineEdit_StockCode)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_Start = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Start.sizePolicy().hasHeightForWidth())
        self.label_Start.setSizePolicy(sizePolicy)
        self.label_Start.setObjectName("label_Start")
        self.horizontalLayout_2.addWidget(self.label_Start)
        self.dateEdit_Start = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_Start.sizePolicy().hasHeightForWidth())
        self.dateEdit_Start.setSizePolicy(sizePolicy)
        self.dateEdit_Start.setMinimumSize(QtCore.QSize(130, 0))
        self.dateEdit_Start.setMaximumSize(QtCore.QSize(130, 16777215))
        self.dateEdit_Start.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_Start.setCalendarPopup(True)
        self.dateEdit_Start.setObjectName("dateEdit_Start")
        self.horizontalLayout_2.addWidget(self.dateEdit_Start)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_End = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_End.sizePolicy().hasHeightForWidth())
        self.label_End.setSizePolicy(sizePolicy)
        self.label_End.setObjectName("label_End")
        self.horizontalLayout.addWidget(self.label_End)
        self.dateEdit_End = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_End.sizePolicy().hasHeightForWidth())
        self.dateEdit_End.setSizePolicy(sizePolicy)
        self.dateEdit_End.setMinimumSize(QtCore.QSize(130, 0))
        self.dateEdit_End.setMaximumSize(QtCore.QSize(130, 16777215))
        self.dateEdit_End.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_End.setCalendarPopup(True)
        self.dateEdit_End.setObjectName("dateEdit_End")
        self.horizontalLayout.addWidget(self.dateEdit_End)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(200, 680))
        self.treeWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setAutoScrollMargin(3)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setColumnCount(0)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout.addWidget(self.treeWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableViewMain = QtWidgets.QTableView(self.centralwidget)
        self.tableViewMain.setMinimumSize(QtCore.QSize(680, 595))
        self.tableViewMain.setObjectName("tableViewMain")
        self.verticalLayout_2.addWidget(self.tableViewMain)
        self.textEditMessage = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditMessage.setMinimumSize(QtCore.QSize(680, 150))
        self.textEditMessage.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textEditMessage.setObjectName("textEditMessage")
        self.verticalLayout_2.addWidget(self.textEditMessage)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 23))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_View = QtWidgets.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        self.menu_Test = QtWidgets.QMenu(self.menubar)
        self.menu_Test.setObjectName("menu_Test")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_New = QtWidgets.QAction(MainWindow)
        self.action_New.setObjectName("action_New")
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Save = QtWidgets.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Show_test = QtWidgets.QAction(MainWindow)
        self.action_Show_test.setObjectName("action_Show_test")
        self.action_Close_test = QtWidgets.QAction(MainWindow)
        self.action_Close_test.setObjectName("action_Close_test")
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Test.addAction(self.action_Show_test)
        self.menu_Test.addAction(self.action_Close_test)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Test.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_StockCode.setText(_translate("MainWindow", "代码名称："))
        self.label_Start.setText(_translate("MainWindow", "开始日期："))
        self.dateEdit_Start.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.label_End.setText(_translate("MainWindow", "结束日期："))
        self.dateEdit_End.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.treeWidget.setSortingEnabled(False)
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_View.setTitle(_translate("MainWindow", "&View"))
        self.menu_Test.setTitle(_translate("MainWindow", "&Test"))
        self.action_New.setText(_translate("MainWindow", "&New"))
        self.action_New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_Save.setText(_translate("MainWindow", "&Save"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_Show_test.setText(_translate("MainWindow", "&Show test"))
        self.action_Close_test.setText(_translate("MainWindow", "&Close test"))
