from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QRadioButton
from PyQt5.QtGui import QPixmap
from PIL import Image
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.current = "orig.jpg"
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('*')

        ## Изображение
        self.pixmap = QPixmap(self.current)
        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(250, 250)
        self.image.setPixmap(self.pixmap)

        ## Оставить один из каналов
        self.channel = [QPushButton(self) for i in range(4)]
        self.channel[0].setText('R')
        self.channel[1].setText('G')
        self.channel[2].setText('B')
        self.channel[3].setText('All')
        for i in range(4):
            self.channel[i].move(20, 30 * i)
            self.channel[i].clicked.connect(self.run)

        self.rotate_btn = QPushButton('Направо', self)
        self.rotate_btn.clicked.connect(self.rotate)
        self.rotate_btn.move(230, 320)

        self.rotate_btn = QPushButton('Налево', self)
        self.rotate_btn.clicked.connect(self.rotate)
        self.rotate_btn.move(90, 320)

    ## В зависимости от нажатой кнопки останется один из каналов или все
    def run(self):
        im = Image.open("orig.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if (self.sender().text() == 'R'):
                    pixels[i, j] = r, 0, 0
                elif (self.sender().text() == 'G'):
                    pixels[i, j] = 0, g, 0
                elif (self.sender().text() == 'B'):
                    pixels[i, j] = 0, 0, b
                else:
                    pass
        im.save("upd.jpg")
        self.pixmap.load("upd.jpg")
        self.current = "upd.jpg"
        self.image.setPixmap(self.pixmap)

    ## Поворот на 90 градусов по/против часовой стрелки в зависимости от нажатой кнопки
    def rotate(self):
        im = Image.open(self.current)
        if (self.sender().text() == "Направо"):
            degree = -90
        else:
            degree = 90
        im2 = im.rotate(degree, expand=True)
        im2.save("upd.jpg")
        self.pixmap.load("upd.jpg")
        self.current = "upd.jpg"
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
