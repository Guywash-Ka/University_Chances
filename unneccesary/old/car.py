import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Координаты')
        self.pixmap = QPixmap('car.jpg')
        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(236, 156)
        self.image.setPixmap(self.pixmap)
        self.show()

        

    def mouseMoveEvent(self, event):
        self.image.move(event.x() - 25, event.y() - 25)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.pixmap = QPixmap('car2.jpg')
            self.image = QLabel(self)
            self.image.move(80, 60)
            self.image.resize(236, 156)
            self.image.setPixmap(self.pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())