import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem

 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ser1.ui',self)
        self.btn_find.clicked.connect(self.search)
        self.out_result.setColumnCount(5)
        self.out_result.setRowCount(1)
        self.out_result.setHorizontalHeaderLabels(['Id', 'Название', 'Год', 'Жанр ID', 'Длительность'])

    def search(self):
        try:
            if self.box_name.isChecked():
                out = self.request(1, self.text_name.text())
            elif self.box_year.isChecked():
                out = self.request(2, self.text_year.text())
            elif self.box_duration.isChecked():
                out = self.request(3, self.text_duration.text())
            print(out)
            for i in range(5):
                self.out_result.setItem(0, i, QTableWidgetItem(str(out[i])))
            self.out_result.resizeColumnsToContents()
        except Exception as e:
            print(e)

    def request(self, param, item):
        con = sqlite3.connect('films.db')
        cur = con.cursor()
        if param == 1:
            ask = '''SELECT * FROM Films AS f WHERE f.title = "{}"'''.format(item)
        elif param == 2:
            ask = '''SELECT * FROM Films AS f WHERE f.year = {}'''.format(int(item))
        elif param == 3:
            ask = '''SELECT * FROM Films AS f WHERE f.duration = {}'''.format(int(item))

        result = cur.execute(ask).fetchall()
        result.sort(key=lambda x: int(x[0]))
        print(result[0])
        return result[0]
        
        

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
