
import PyQt5
from PyQt5 import QtWidgets, QtGui

from wgpu.gui.qt import WgpuCanvas
import wgpu.backends.rs  # noqa: F401, Select Rust backend

from triangle import main


class ExampleWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        self.setWindowTitle("wgpu triangle embedded in a qt app")

        splitter = QtWidgets.QSplitter()

        self.button = QtWidgets.QPushButton("Hello world", self)
        self.canvas1 = WgpuCanvas(splitter)
        self.canvas2 = WgpuCanvas(splitter)

        splitter.addWidget(self.canvas1)
        splitter.addWidget(self.canvas2)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.button, 0)
        layout.addWidget(splitter, 1)
        self.setLayout(layout)

        self.show()

    def actionEvent(self, a0: QtGui.QActionEvent) -> None:
        print(a0)


app = QtWidgets.QApplication([])
example = ExampleWidget()

main(example.canvas1)
main(example.canvas2)

# Enter Qt event loop (compatible with qt5/qt6)
app.exec() if hasattr(app, "exec") else app.exec_()