import PyQt5
from PyQt5 import QtWidgets, QtGui

import pygame as pg


class Subscriber:
    def update(self):
        return NotImplemented(f"update() not implemented in the {self.__name__}")


class PygameWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PygameWidget, self).__init__(parent)
        self.resize(640, 480)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.w = a0.size().width()
        self.h = a0.size().height()
        self.updatePyGame()
        super().resizeEvent(a0)

    def updatePyGame(self):
        self.s = pg.Surface((self.w, self.h))
        self.bg_color = (50, 50, 50, 255)
        self.s.fill(self.bg_color)
        self.data = self.s.get_buffer().raw
        self.image = QtGui.QImage(self.data, self.w, self.h, QtGui.QImage.Format_RGB32)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.image)
        qp.end()


class View(PygameWidget, Subscriber):
    def __init__(self, model):
        PygameWidget.__init__(self)
        self.model = model
        self.model.addSubscriber(self)

    def update(self):
        self.repaint()


