import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QRadioButton, QVBoxLayout
import PyQt5.QtGui as QtGui

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1000, 600, 300, 100)
        self.setWindowTitle('Кто отправил сигнал')

        self.first_player = QRadioButton('X', self)
        self.first_player.move(50, 40)

        self.first_player1 = QRadioButton('0', self)
        self.first_player1.move(130, 40)

        self.btn = QPushButton('Play!', self)
        self.btn.move(200, 40)
        self.btn.clicked.connect(self.run)
        

        #self.radio_button_1 = QRadioButton('1')
        #self.radio_button_1.move(100, 0)
        #layout = QVBoxLayout()
        #layout.addWidget(self.radio_button_1)
        #self.setLayout(layout)

        self.show()

    def run(self):
        if self.first_player.isChecked():
            player = 'X'
        else:
            player = '0'
        self.second_form = SecondForm(player)
        self.second_form.show()


class SecondForm(QWidget):
    def __init__(self, args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.player = args
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('________')

        self.buttons = [[], [], []]

        self.btn1 = QPushButton(self)
        self.btn1.resize(200, 200)
        self.btn1.move(0, 0)
        self.btn1.clicked.connect(self.run)
        self.buttons[0].append(self.btn1)
        
        self.btn2 = QPushButton(self)
        self.btn2.resize(200, 200)
        self.btn2.move(200, 0)
        self.btn2.clicked.connect(self.run)
        self.buttons[0].append(self.btn2)
        
        self.btn3 = QPushButton(self)
        self.btn3.resize(200, 200)
        self.btn3.move(400, 0)
        self.btn3.clicked.connect(self.run)
        self.buttons[0].append(self.btn3)

        self.btn4 = QPushButton(self)
        self.btn4.resize(200, 200)
        self.btn4.move(0, 200)
        self.btn4.clicked.connect(self.run)
        self.buttons[1].append(self.btn4)

        self.btn5 = QPushButton(self)
        self.btn5.resize(200, 200)
        self.btn5.move(200, 200)
        self.btn5.clicked.connect(self.run)
        self.buttons[1].append(self.btn5)

        self.btn6 = QPushButton(self)
        self.btn6.resize(200, 200)
        self.btn6.move(400, 200)
        self.btn6.clicked.connect(self.run)
        self.buttons[1].append(self.btn6)

        self.btn7 = QPushButton(self)
        self.btn7.resize(200, 200)
        self.btn7.move(0, 400)
        self.btn7.clicked.connect(self.run)
        self.buttons[2].append(self.btn7)

        self.btn8 = QPushButton(self)
        self.btn8.resize(200, 200)
        self.btn8.move(200, 400)
        self.btn8.clicked.connect(self.run)
        self.buttons[2].append(self.btn8)

        self.btn9 = QPushButton(self)
        self.btn9.resize(200, 200)
        self.btn9.move(400, 400)
        self.btn9.clicked.connect(self.run)
        self.buttons[2].append(self.btn9)
    
    def run(self):
        if not self.sender().text():
            #print(self.buttons[0].index(self.sender()))
            self.sender().setText(self.player)
            self.change_player()
            self.check_winner()
        
    def change_player(self):
        if self.player == 'X':
            self.player = '0'
        else:
            self.player = 'X'
    
    def check_winner(self):
        WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        for row in WAYS_TO_WIN:
            if self.buttons[row[0]] == board[row[1]]==board[row[2]] != EMPTY:
                winner = board[row[0]]
                return winner
                


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())