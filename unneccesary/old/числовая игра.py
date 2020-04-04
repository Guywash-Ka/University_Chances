import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber, QLineEdit
 

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.Y = random.randint(6, 11)
        self.X = random.randint(1, 20)
        self.Z = random.randint(6, 11)
        self.count = 0

        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Пятая программа')

        self.label = QLabel(self)
        self.label.setText(f"X: {self.X}")
        self.label.move(30, 10)

        self.btnY = QPushButton(f'Увеличить на {self.Y}', self)
        self.btnY.resize(self.btnY.sizeHint())
        self.btnY.move(70, 130)
        self.btnY.clicked.connect(self.hello)

        self.btnZ = QPushButton(f'Уменьшить на {self.Z}', self)
        self.btnZ.resize(self.btnZ.sizeHint())
        self.btnZ.move(70, 170)
        self.btnZ.clicked.connect(self.hello)

        self.summa = QLCDNumber(self)
        self.summa.move(70, 200)

    def hello(self):
        if self.count == 10:
            self.second = SecondForm(self, 'U LOSER!!!')
            self.second.show()
        if self.sender() == self.btnY:
            self.X += self.Y
            self.label.setText(f'X: {self.X}')
            self.label.resize(self.label.sizeHint())
        else:
            self.X -= self.Z
            self.label.setText(f'X: {self.X}')
            self.label.resize(self.label.sizeHint())
        if self.X == 0:
            self.second = SecondForm(self, 'Congratulations!!!')
            self.second.show()
        self.count += 1
        self.summa.display(self.count)

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