import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber, QLineEdit
 

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.string = ''

        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Пятая программа')

        self.btn = QPushButton('*', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(0, 40)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('/', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(0, 65)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('+', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(0, 89)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('-', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(0, 113)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('1', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(81, 88)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('2', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(162, 88)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('3', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(243, 88)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('4', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(81, 64)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('5', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(162, 64)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('6', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(243, 64)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('7', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(81, 40)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('8', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(162, 40)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('9', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(243, 40)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('0', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(162, 112)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('CE', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(243, 112)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('=', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(324, 40)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('.', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(81, 112)
        self.btn.clicked.connect(self.hello)

        self.summa = QLabel(self)
        self.summa.move(0, 0)
        self.summa.resize(400, 40)

    def can_write(self, a):
        if '=' in self.string:
            return False
        if self.string == '':
            return True
        if a in '*/+':
            if self.string[-1].isdigit():
                return True
            return False
        elif a == '-':
            if self.string[-1] in '*/+-' and self.string[-2] in '/*-+':
                return False
            return True
        elif a == '.':
            if (self.string[-1] in '*/+-') or (len(self.string) == 0):
                return False
            i = 0
            while (not self.string[-i+1] in '*/+-') and (i < len(self.string)):
                if self.string[-i] == '.':
                    return False
                i += 1
            return True
        return True

    def result(self):
        res = 0
        numb = 0
        znak = ''
        for i in range(len(self.string)):
            self.string[i] = ch
            if ch.isdigit():
                numb = numb * 10 + int(ch)
            elif ch == '+':
                res += numb
                numb = 0
            elif ch == '-':
                if  

    def hello(self):
        if self.sender().text() == '=':
            self.string += '= ' + self.result()
        elif self.sender().text() == 'CE':
            self.string = ''
        elif self.can_write(self.sender().text()):
            self.string += self.sender().text()
        self.summa.setText(self.string)
        #if second == 0:
        #    self.second_form = SecondForm(self, 'Eror: cannot take "0" as a second number.')
         #   self.second_form.show()


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Вторая форма')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())