import sys
from random import randint

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(250, 150)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):
        r = randint(50, 250)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(0, 0, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
