import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('genre_filtration.ui', self)

        con = sqlite3.connect('films.db')
        cur = con.cursor()
        genres = cur.execute("""SELECT title FROM genres""").fetchall()
        genres = [value[0] for value in genres]
        self.comboBox.addItems(genres)

        self.pushButton.clicked.connect(self.print)

    def print(self):
        con = sqlite3.connect('films.db')
        cur = con.cursor()

        genre = str(self.comboBox.currentText())
        result = cur.execute("""SELECT title FROM Films WHERE genre=(SELECT id FROM genres 
                            WHERE title = '""" + genre + '\')').fetchall()
        result = [value[0] for value in result]
        self.listWidget.clear()
        self.listWidget.addItems(result)


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())