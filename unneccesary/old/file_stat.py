import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber
 

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('file_stat')
        self.mini, self.maxi, self.ave = self.read_file()

        self.label = QLabel(self)
        self.label.setText("Minimum:")
        self.label.move(80, 30)

        self.label1 = QLabel(self)
        self.label1.setText("Maximum:")
        self.label1.move(80, 100)

        self.label2 = QLabel(self)
        self.label2.setText("Average:")
        self.label2.move(80, 170)

        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(110, 70)
        self.LCD_count.display(self.mini)

        self.LCD_count1 = QLCDNumber(self)
        self.LCD_count1.move(110, 140)
        self.LCD_count1.display(self.maxi)

        self.LCD_count2 = QLCDNumber(self)
        self.LCD_count2.move(110, 210)
        self.LCD_count2.display(self.ave)

    def read_file(self):
        d = open('output.txt', mode='w')
        with open('input.txt') as f:
            s = f.read().split()
        mini = min([int(i) for i in s])
        maxi = max([int(i) for i in s])
        ave = sum([int(i) for i in s]) / len(s)
        d.write(f'min: {mini}, max: \
            {maxi}, average: {ave}')
        return mini, maxi, ave
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())