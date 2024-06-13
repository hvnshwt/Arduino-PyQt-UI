# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plane = QtWidgets.QGraphicsView(self.centralwidget)
        self.plane.setGeometry(QtCore.QRect(10, 50, 321, 301))
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.plane.setBackgroundBrush(brush)
        self.plane.setObjectName("plane")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 161, 16))
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(340, 50, 256, 301))
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 30, 161, 16))
        self.label_2.setObjectName("label_2")
        self.settings_boc = QtWidgets.QGroupBox(self.centralwidget)
        self.settings_boc.setGeometry(QtCore.QRect(610, 50, 221, 301))
        self.settings_boc.setTitle("")
        self.settings_boc.setObjectName("settings_boc")
        self.label_4 = QtWidgets.QLabel(self.settings_boc)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(self.settings_boc)
        self.widget.setGeometry(QtCore.QRect(10, 30, 201, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.open_btn = QtWidgets.QPushButton(self.widget)
        self.open_btn.setObjectName("open_btn")
        self.horizontalLayout.addWidget(self.open_btn)
        self.close_btn = QtWidgets.QPushButton(self.widget)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 30, 161, 16))
        self.label_3.setObjectName("label_3")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(250, 360, 75, 23))
        self.start_btn.setObjectName("start_btn")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(760, 360, 75, 23))
        self.exit_btn.setObjectName("exit_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Положение на плоскости"))
        self.label_2.setText(_translate("MainWindow", "Последние перемещения"))
        self.label_4.setText(_translate("MainWindow", "Serial Port"))
        self.open_btn.setText(_translate("MainWindow", "Open"))
        self.close_btn.setText(_translate("MainWindow", "Close"))
        self.label_3.setText(_translate("MainWindow", "Настройки"))
        self.start_btn.setText(_translate("MainWindow", "Начать"))
        self.exit_btn.setText(_translate("MainWindow", "Выход"))
