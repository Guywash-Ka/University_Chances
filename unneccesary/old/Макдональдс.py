import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber, QLineEdit, QCheckBox, QPlainTextEdit
from PyQt5.QtCore import Qt
 

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.products = []
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Пятая программа')

        self.label = QLabel(self)
        self.label.setText("Выберите продукты:")
        self.label.move(30, 10)

        self.dishes = QCheckBox('Чикенбургер', self)
        self.dishes.move(20, 40)
        #self.dishes.stateChanged.connect(self.changeTitle)
        self.products.append(self.dishes)

        self.dishes1 = QCheckBox('Чизбургер', self)
        self.dishes1.move(200, 40)
        #self.dishes1.stateChanged.connect(self.changeTitle)
        self.products.append(self.dishes1)

        self.dishes2 = QCheckBox('Маккомбо с БигМаком', self)
        self.dishes2.move(20, 100)
        #self.dishes2.stateChanged.connect(self.changeTitle)
        self.products.append(self.dishes2)

        self.dishes3 = QCheckBox('Картошка по-деревенски', self)
        self.dishes3.move(200, 100)
        #self.dishes3.stateChanged.connect(self.changeTitle)
        self.products.append(self.dishes3)

        #self.check = QPlainTextEdit(self)
        #self.check.move(50, 100)
        self.btn = QPushButton('Go!', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(160, 150)
        self.btn.clicked.connect(self.hello)
    def hello(self):
        res = ''
        for i in self.products:
            if i.checkState():
                res += i.text() + '_'
        self.open_second_form(self.print_check(res[:-1]))

    def open_second_form(self, info):
        self.second_form = SecondForm(self, info)
        self.second_form.show()
    
    def print_check(self, string):
        res = ''
        string = string.split('_')
        for i in string:
            res += i + ' - 1шт.\n'
        return res


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('________')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())