from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import csv


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 321, 491))
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 520, 311, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 22))
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


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setupUi(self)
        self.tableWidget.itemChanged.connect(self.cellChanged)

        with open("input.csv", encoding="utf-8") as f:
            r = csv.reader(f, delimiter=";")
            items = sorted([(i[0], int(i[1])) for i in r], key=lambda x: x[1])

            for i in range(len(items)):
                self.tableWidget.insertRow(i)
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(items[i][0]))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(items[i][1])))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem("0"))

    def cellChanged(self):
        total = 0
        for row in range(self.tableWidget.rowCount()):
            try:
                price = int(self.tableWidget.item(row, 1).text())
                count = int(self.tableWidget.item(row, 2).text())
                total += price * count
            except Exception:
                pass
        self.lcdNumber.display(total)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()