import sys
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from random import randint


class ColoredEllipses(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.x = 0
        self.y = 0
        self.do = False

    def initUI(self):
        self.setWindowTitle("Not Car")
        self.button = QPushButton(self)
        self.button.setGeometry(300, 500, 100, 40)
        self.button.setText("click me")
        self.button.clicked.connect(self.painting)
        self.setGeometry(100, 100, 700, 700)

    def paintEvent(self, event):
        if self.do:
            qp = QPainter()
            qp.begin(self)
            d = randint(20, 100)
            r, g, b = self.random_color()
            qp.setBrush(QColor(r, g, b))
            self.x, self.y = randint(0, 699), randint(0, 699)
            qp.drawEllipse(QPointF(self.x, self.y), d, d)
            self.do = False
            qp.end()

    def painting(self):
        self.do = True
        self.repaint()

    def random_color(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return r, g, b

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ColoredEllipses()
    ex.show()
    sys.exit(app.exec())