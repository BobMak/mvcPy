import sys

import PyQt5
from PyQt5 import QtWidgets
import pygame as pg

from TestFactory import TestFactory
from mvc.App import MainWindow


class TestApp(MainWindow):
    def __init__(self, factory):
        MainWindow.__init__(self, factory)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    pg.init()
    w = TestApp(TestFactory())
    w.show()
    app.exec_()