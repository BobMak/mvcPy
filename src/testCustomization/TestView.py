from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import pygame as pg

from mvc.View import View


class TestView(View):
    def __init__(self, parent=None):
        View.__init__(self, parent)

    def update(self):
        self.s.fill(self.bg_color)
        for x in self.model.shapes:
            pg.draw.circle(self.s, (55,200,55,125), (x[0],x[1]), x[2])
        self.data = self.s.get_buffer().raw
        self.image = QtGui.QImage(self.data, self.w, self.h, QtGui.QImage.Format_RGB32)
        self.repaint()


