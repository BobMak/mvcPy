import sys

import PyQt5
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import pygame as pg

from mvc.Factory import Factory


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, factory, parent=None):
        super(MainWindow,self).__init__(parent)
        # self.button = QtWidgets.QPushButton("Hello world", self)
        self.commands = []
        self.factory = factory
        self.model = factory.makeModel()
        self.main_widget = factory.makeView(self.model)
        self.setCentralWidget(self.main_widget)
        self.resize(640, 480)
        x = QtWidgets.QHBoxLayout(self.main_widget)
        tb = self.createToolbar()
        x.addWidget(tb)
        x.setAlignment(Qt.AlignTop)
        self.createMenus()
        self.createActions()
        self.setLayout(x)
        self.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')

    def actionEvent(self, a0: QtGui.QActionEvent) -> None:
        print(a0)

    def createActions(self):
        # Edit menu
        edit_menu = self.menuBar().addMenu("Edit")
        commands = self.factory.getEditCommands()
        for c in commands:
            qa = QtWidgets.QAction(c, self)
            com = self.factory.makeCommand(self.model, c)
            edit_menu.addAction(qa)
            self.commands.append(com)
            # maybe storing a factory call is better, but idk how to pass parameters here
            qa.triggered.connect(com.execute)

    def createMenus(self):
        menu_bar = QtWidgets.QMenuBar()
        self.setMenuBar(menu_bar)

    def createToolbar(self):
        tool_bar = QtWidgets.QToolBar()
        commands = self.factory.getToolBarCommands()
        for c in commands:
            qa = QtWidgets.QAction(c, self)
            com = self.factory.makeCommand(self.model, c)
            self.commands.append(com)
            tool_bar.addAction(qa)
            qa.triggered.connect(com.execute)
        return tool_bar


# todo fix the app continuing to run after the main window is closed
def main():
    app = QtWidgets.QApplication(sys.argv)
    pg.init()
    w = MainWindow(Factory())
    w.show()
    app.exec_()


if __name__ == "__main__":
    main()
