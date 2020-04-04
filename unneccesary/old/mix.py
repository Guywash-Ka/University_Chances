import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber
 

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 700, 300)
        self.setWindowTitle('Пятая программа')

        f = open('text.txt').readlines()

        self.label = QLabel(self)
        self.label.setText("ЧЕТНЫЕ СТРОКИ")
        self.label.move(5, 10)
        
        j = 30
        for i in f[1::2]:
            self.label1 = QLabel(self)
            self.label1.setText(i)
            self.label1.move(35, j)
            j += 20
        
        self.label = QLabel(self)
        self.label.setText("НЕЧЕТНЫЕ СТРОКИ")
        self.label.move(370, 10)

        j = 30
        for i in f[::2]:
            self.label1 = QLabel(self)
            self.label1.setText(i)
            self.label1.move(385, j)
            j += 20

        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())