import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Координаты')
        self.btn = QPushButton(self)
        self.btn.move(100, 100)
        self.btn.resize(50, 50)
        self.coords = QLabel(self)
        self.coords.setText("Координаты:None, None")
        self.coords.move(30, 30)
        self.show()

        

    def mouseMoveEvent(self, event):
        self.coords.setText("Координаты:{}, {}".format(
            event.x(), event.y()))
        print(self.btn.x() - event.x(), self.btn.y() - event.y())
        if (-20 < self.btn.x() - event.x() < 20) and (-85 < self.btn.y() - event.y() < 15):
            self.btn.move(self.btn.x() + 20, self.btn.y())
        elif (-70 < self.btn.x() - event.x() < -20) and (-85 < self.btn.y() - event.y() < 15):
            self.btn.move(self.btn.x() -20, self.btn.y())
        if (-70 < self.btn.x() - event.x() < 20) and (-85 < self.btn.y() - event.y() < -35):
            self.btn.move(self.btn.x(), self.btn.y() - 20)
        elif (-70 < self.btn.x() - event.x() < 20) and (-35 < self.btn.y() - event.y() < 15):
            self.btn.move(self.btn.x(), self.btn.y() + 20)
        if not 50 < self.btn.x() < 550:
            self.btn.move(250, 250)
        if not 50 < self.btn.y() < 550:
            self.btn.move(250, 250)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())