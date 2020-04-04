import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

 
class MyWidget(QMainWindow):
    def __init__(self):
        self.st = ""
        super().__init__()
        uic.loadUi('beautiful_calc.ui', self)
        self.b1.clicked.connect(lambda: self.add_text("1"))
        self.b2.clicked.connect(lambda: self.add_text("2"))
        self.b3.clicked.connect(lambda: self.add_text("3"))
        self.b4.clicked.connect(lambda: self.add_text("4"))
        self.b5.clicked.connect(lambda: self.add_text("5"))
        self.b6.clicked.connect(lambda: self.add_text("6"))
        self.b7.clicked.connect(lambda: self.add_text("7"))
        self.b8.clicked.connect(lambda: self.add_text("8"))
        self.b9.clicked.connect(lambda: self.add_text("9"))
        self.b0.clicked.connect(lambda: self.add_text("0"))
        self.bplus.clicked.connect(lambda: self.add_text("+"))
        self.bminus.clicked.connect(lambda: self.add_text("-"))
        self.bmul.clicked.connect(lambda: self.add_text("*"))
        self.bover.clicked.connect(lambda: self.add_text("/"))
        self.bfact.clicked.connect(lambda: self.add_text("fact("))
        self.bsqrt.clicked.connect(lambda: self.add_text("sqrt("))
        self.bpow.clicked.connect(lambda: self.add_text("^"))
        self.bopen.clicked.connect(lambda: self.add_text("("))
        self.bclose.clicked.connect(lambda: self.add_text(")"))

        self.bdel1.clicked.connect(self.pop)
        self.bclr.clicked.connect(self.clear)

        self.beq.clicked.connect(self.count)

    def add_text(self, t):
        if self.mainlabel.text() in ["0", "ERROR!"]:
            self.mainlabel.setText(t)
            self.update()
            return
        self.mainlabel.setText(self.mainlabel.text() + t)
        self.update()
        
    def update(self):
        if not self.mainlabel.text():
            self.clear()
        # self.hide()
        # self.show()

    def clear(self):
        self.mainlabel.setText("0")
        self.update()

    def pop(self):
        self.mainlabel.setText(self.mainlabel.text()[:-1])
        self.update()

    def count(self):
        def sqrt(x):
            if x < 0:
                raise ValueError
            return x ** 0.5

        def fact(j):
            x = 1
            for i in range(2, j + 1):
                x *= i
            return x
        
        t = self.mainlabel.text()
        t = t.replace("^", "**")
        try:
            self.mainlabel.setText(str(eval(t)))
        except:
            self.mainlabel.setText("ERROR!")
        self.update()
 

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
