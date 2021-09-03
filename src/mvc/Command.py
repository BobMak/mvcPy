from PyQt5 import QtWidgets

class Command:
    def __init__(self, model, id):
        self.model = model

    def getQTWidget(self):
        return QtWidgets.QAction

    def execute(self):
        print("executing")
        # return NotImplemented()