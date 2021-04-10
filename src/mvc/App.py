import random
import sys
import pyglet
from PySide6 import QtCore, QtGui, QtOpenGL, QtWidgets

from utils.QTPygletWidget import QPygletWidget


class MyPygletWidget(QPygletWidget):
    def on_init(self):
        self.sprite = pyglet.sprite.Sprite(pyglet.resource.image("logo.png"))
        self.label = pyglet.text.Label(
            text="This is a pyglet label rendered in a Qt widget :)")
        self.setMinimumSize(QtCore.QSize(640, 480))

    def on_draw(self):
        self.sprite.draw()
        self.label.draw()

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

def main():
    app = QtWidgets.QApplication([])
    # widget = MyWidget()
    widget = MyPygletWidget()
    widget.resize(800, 600)
    widget.show()
    # app.activeWindow()
    # app.
    # window = QtWidgets.QWidget()
    # window.setCentralWidget(widget)
    # window.show()
    # # app.connect(widget)
    sys.exit(app.exec_()) #


if __name__ == "__main__":
    main()
