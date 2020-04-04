import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QInputDialog
from math import *
x_s, y_s = 300, 300


def countk(x1, y1, x2, y2, k):
    return x1 + (x2 - x1) * k, y1 + (y2 - y1) * k


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.p = 3
        self.k = k
        self.n = n
        self.a = a
        i, okBtnPressed = QInputDialog.getItem(self, "Выберите цвет", 
                                       "Цвет", 
                                       ("Красный", "Зеленый", "Синий"), 
                                       1, False)
        self.colo = i
        if not okBtnPressed:
            sys.exit()
        self.setGeometry(0, 0, x_s, y_s)
        self.setWindowTitle('Квадрат объектив')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawQuad(qp)
        qp.end()

    def xs(self, x):
        return x + x_s // 2

    def ys(self, y):
        return y_s // 2 - y

    def drawQuad(self, qp):
        if self.colo == 'Зеленый':
            pen = QPen(Qt.green, 2)
        elif self.colo == 'Красный':
            pen = QPen(Qt.red, 2)
        elif self.colo == 'Синий':
            pen = QPen(Qt.blue, 2)
        qp.setPen(pen)
        try:
            RAD = self.a
            p = self.p
            nodes = [(RAD * cos(i * 2 * pi / p + pi / p), RAD * sin(i * 2 * pi / p + pi / p)) for i in range(p)]
            nodes2 = [(self.xs(node[0]), self.ys(node[1])) for node in nodes]
            new = []
            for i in range(self.n):
                for i in range(-1, len(nodes2) - 1):
                    new.append(countk(*nodes[i], *nodes[i + 1], self.k))
                    qp.drawLine(*nodes2[i], *nodes2[i + 1])
                nodes = new.copy()
                nodes2 = [(self.xs(node[0]), self.ys(node[1])) for node in nodes]
                new = []
        except Exception:
            pass

print('Введите k')
k = float(input())
print('Введите n')
n = int(input())
print('Введите длину стороны')
a = int(input())
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
