# Form implementation generated from reading ui file 'externalSortsPSU.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 291)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 761, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(153, 43, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(153, 72, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(153, 102, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(154, 132, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(154, 162, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.simple2f = QtWidgets.QCheckBox(self.centralwidget)
        self.simple2f.setGeometry(QtCore.QRect(80, 40, 21, 21))
        self.simple2f.setText("")
        self.simple2f.setObjectName("simple2f")
        self.simple1f = QtWidgets.QCheckBox(self.centralwidget)
        self.simple1f.setGeometry(QtCore.QRect(80, 70, 21, 21))
        self.simple1f.setText("")
        self.simple1f.setObjectName("simple1f")
        self.natural2f = QtWidgets.QCheckBox(self.centralwidget)
        self.natural2f.setGeometry(QtCore.QRect(80, 100, 21, 21))
        self.natural2f.setText("")
        self.natural2f.setObjectName("natural2f")
        self.natural1f = QtWidgets.QCheckBox(self.centralwidget)
        self.natural1f.setGeometry(QtCore.QRect(80, 130, 21, 21))
        self.natural1f.setText("")
        self.natural1f.setObjectName("natural1f")
        self.absorb = QtWidgets.QCheckBox(self.centralwidget)
        self.absorb.setGeometry(QtCore.QRect(80, 160, 21, 21))
        self.absorb.setText("")
        self.absorb.setObjectName("absorb")
        self.sort = QtWidgets.QPushButton(self.centralwidget)
        self.sort.setGeometry(QtCore.QRect(20, 200, 131, 41))
        self.sort.setObjectName("sort")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 210, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.size = QtWidgets.QSpinBox(self.centralwidget)
        self.size.setGeometry(QtCore.QRect(334, 207, 81, 24))
        self.size.setObjectName("size")
        self.size.setProperty("value", 10000)
        self.size.setMaximum(1000000000)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 210, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.OP = QtWidgets.QSpinBox(self.centralwidget)
        self.OP.setGeometry(QtCore.QRect(540, 207, 81, 24))
        self.OP.setObjectName("OP")
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(700, 200, 71, 41))
        self.quit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../SortsUniversity/LR_11-14/1617409.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.quit.setIcon(icon)
        self.quit.setObjectName("quit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ЛР22-26 Антонов 21ВП2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Сравнения"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Присвоения"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Время"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Отсортировано?"))
        self.label.setText(_translate("MainWindow", "Простое 2ф"))
        self.label_2.setText(_translate("MainWindow", "Простое 1ф"))
        self.label_3.setText(_translate("MainWindow", "Естественное 2ф"))
        self.label_4.setText(_translate("MainWindow", "Естественное 1ф"))
        self.label_5.setText(_translate("MainWindow", "Поглощение"))
        self.sort.setText(_translate("MainWindow", "Сортировать"))
        self.label_6.setText(_translate("MainWindow", "Размер массива"))
        self.label_7.setText(_translate("MainWindow", "% ОП"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
