import sys
from random import choice
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QButtonGroup


class MyWidget(QMainWindow):
    def __init__(self, matrix):
        super().__init__()
        
        h = len(matrix)
        w = len(matrix[0])

        self.setGeometry(100, 100, w * b, h * b)

        self.btn_matrix = []
        self.all_g = QButtonGroup(self)
        
        for i in range(h):
            self.btn_matrix.append([])
            for j in range(w):
                self.btn_matrix[i].append(QPushButton(self))
                self.btn_matrix[i][j].setGeometry(b * j, b * i, b, b)
                color = "white" if matrix[i][j] else "black"
                self.btn_matrix[i][j].ccolor = color
                self.btn_matrix[i][j].setStyleSheet('QPushButton {background-color: ' + color + ';}')
                self.all_g.addButton(self.btn_matrix[i][j])

        self.all_g.buttonClicked.connect(self.update_btn)

    def update_btn(self, btn):
        btn.ccolor = "white" if btn.ccolor == "black" else "black"
        btn.setStyleSheet('QPushButton {background-color: ' + btn.ccolor + ';}')
        return
        self.hide()
        self.show()


w = 20
h = 20
b = 40  # размер кнопки
# Изначально генерируется случайная пиксель-последовательность.
# По нажатию на кнопку цвет инвертируется. Так можно рисовать.
matrix = [[choice([0, 1]) for i in range(w)] for j in range(h)]
app = QApplication(sys.argv)
ex = MyWidget(matrix)
ex.show()
sys.exit(app.exec_())