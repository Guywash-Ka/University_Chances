import sys
import csv
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("form.ui", self)

        self.translator = {"Название": "title", "Год выпуска": "year",
                      "Длительность": "duration"}

        for key in self.translator.keys():
            self.combo.addItem(key)

        self.table.setRowCount(1)
        self.table.setColumnCount(4)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.search_button.clicked.connect(self.search)
            

    def search(self):
        item = self.combo.currentText()
        key = self.translator[item]
        value = self.input.text()
        operator = self.operator_input.text()

        cursor.execute(f"SELECT * FROM films WHERE {key} {operator} '{value}' ORDER BY ID")
        result = cursor.fetchone()
        
        if not result:
            return

        self.table.setItem(0, 0, QTableWidgetItem(result[1]))
        self.table.setItem(0, 1, QTableWidgetItem(str(result[2])))
        self.table.setItem(0, 2, QTableWidgetItem(str(result[3])))
        self.table.setItem(0, 3, QTableWidgetItem(str(result[4])))
        

conn = sqlite3.connect("films.db")
cursor = conn.cursor()

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
