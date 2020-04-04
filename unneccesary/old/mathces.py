import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import time

 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('matches.ui',self)
        self.buttonGroup.buttonClicked.connect(self.run)
        self.matches = 37
        self.label.setText('| ' * self.matches + f'({self.matches} matches left)')
    
    def run(self):
        if self.one.isChecked():
            a = self.one.text()
        if self.two.isChecked():
            a = self.two.text()
        if self.four.isChecked():
            a = self.four.text()
        if self.five.isChecked():
            a = self.five.text()
        if self.three.isChecked():
            a = self.three.text()
        if int(a) == self.matches:
            self.listWidget.addItem(f'You: {a}')
            self.label.setText('You win!')
        elif int(a) < self.matches:
            self.listWidget.addItem(f'You: {a}')
            self.matches -= int(a)
            self.label.setText('| ' * self.matches + f'({self.matches} matches left)')
        if self.matches < 6:
            self.listWidget.addItem(f'Comp: {3}')
            self.label.setText('Comp won!')
        else:
            self.listWidget.addItem(f'Comp: {3}')
            self.matches -= 3
            self.label.setText('| ' * self.matches + f'({self.matches} matches left)')

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())