import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import uic
from PyQt5.QtGui import QColor
import csv
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("exp.ui", self)
        self.loadTable('prices.csv')

    def loadTable(self, table_name):
        with open(table_name) as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            reader = sorted(list(reader), key=lambda x: -int(x[1]))
            print(reader)
            title = ["Название", "Цена"]
            self.table.setColumnCount(len(title))
            self.table.setHorizontalHeaderLabels(title)
            self.table.setRowCount(0)
            for i, row in enumerate(reader):
                self.table.setRowCount(self.table.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(elem))
                self.table.setItem(i, 2, QTableWidgetItem("0"))
                self.table.setItem(i, 3, QTableWidgetItem("0"))
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i in range(min(5, self.table.rowCount())):
            self.colorRow(i, QColor(randint(0, 255),
                                    randint(0, 255),
                                    randint(0, 255)))


    def colorRow(self, row, color):
        for i in range(self.table.columnCount()):
            self.table.item(row, i).setBackground(color)

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())