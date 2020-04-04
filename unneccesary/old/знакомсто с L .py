import math
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self, stage, x, y, l, name):
        super().__init__()
        self.initUI()
        f = open(name, encoding='utf8')
        lines = f.readlines()
        c = int(lines[1].replace('\n', ''))
        self.ce = 360 // c
        self.x = 250 + x 
        self.y = 250 - y
        self.l = l
        self.stage = stage
        self.teo = lines[2].replace('\n', '')
        a = len(lines)
        lst = {}
        for i in range(a - 3):
            lst[lines[3 + i][0]] = lines[3 + i][2:].replace('\n', '')
        for i in range(stage):
            teo_copy = ''
            for j in range(len(self.teo)):
                if self.teo[j] in lst:
                    teo_copy += lst[self.teo[j]]
                else:
                    teo_copy += self.teo[j]
            self.teo = teo_copy
            print(self.teo)
        self.flag = True

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Рисование')
        self.show()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawFlag(qp)
            qp.end()

    def drawFlag(self, qp):
        c = 0
        lst_copy_x = []
        lst_copy_y = []
        lst_copy_c = []
        for i in self.teo:
            if i == 'F':
                x2 = round(self.x + self.l * math.cos(math.radians(c)))
                y2 = round(self.y + self.l * math.sin(math.radians(c)))
                qp.drawLine(self.x, self.y, x2, y2)
                self.x = x2
                self.y = y2
            elif i == '-':
                c -= self.ce
                if c < 0:
                    c = 360 + c
                c = c % 360                
            elif i == '+':
                c += self.ce
                c = c % 360
            elif i == '[':
                lst_copy_c.append(c)
                lst_copy_x.append(self.x)
                lst_copy_y.append(self.y)
            elif i == ']':
                c = lst_copy_c[-1]
                self.x = lst_copy_x[-1]
                self.y = lst_copy_y[-1]
                del lst_copy_c[-1]
                del lst_copy_x[-1]
                del lst_copy_y[-1]
        self.flag = False


name = input('file_name')
stage = int(input('Phase'))
x = int(input('x'))
y = int(input('y'))
l = int(input('Length'))
app = QApplication(sys.argv)
ex = Example(stage, x, y, l, name)
sys.exit(app.exec_())