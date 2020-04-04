import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from math import pi, cos, sin


SCREEN_SIZE = [400, 400]


class Example(QWidget):
    def __init__(self, p, k, n, a):
        self.p = p
        self.k = k
        self.n = n
        self.a = a
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Объектив')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawStar(qp)
        qp.end()

    def xs(self,x):
        return x + SCREEN_SIZE[0] // 2

    def ys(self,y):
        return SCREEN_SIZE[1] // 2 - y

    def drawStar(self, qp):
        pen = QPen(Qt.red, 2)
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
        except Exception as e:
            print(e)


def countk(x1, y1, x2, y2, k):
    return x1 + (x2 - x1) * k, y1 + (y2 - y1) * k


k = float(input("Введите k: "))
n = int(input("Введите n: "))
a = int(input("Введите длину стороны: "))
app = QApplication(sys.argv)
ex = Example(4, k, n, a)
print(123)
sys.exit(app.exec_())
