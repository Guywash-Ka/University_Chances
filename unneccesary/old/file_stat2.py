from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('file_stat2')
        f = open('input.txt').read()
        d = open('output.txt', mode='w')
        self.maxx, self.minn = self.popularity(f)
        d.write(f'Most popular: {self.maxx[1]}| {self.maxx[0]} times.\
            \n\nLeast popular: {self.minn[1]}| {self.minn[0]} times.')
        self.label = QLabel(self)
        self.label.move(20, 10)
        self.label.setText(f'Most popular: {self.maxx[1]}| {self.maxx[0]} times.\
            \n\nLeast popular: {self.minn[1]}| {self.minn[0]} times.')
        
    
    def popularity(self, string):
        max_c = 0
        min_c = string.count(string[0])
        min_symb = string[0]
        max_symb = ''
        for i in string:
            if i != ' ':
                if string.count(i) > max_c:
                    max_c = string.count(i)
                    max_symb = i
                elif string.count(i) < min_c:
                    min_c = string.count(i)
                    min_symb = i
        return [(max_c, max_symb), (min_c, min_symb)]
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())