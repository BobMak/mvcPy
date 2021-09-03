from PyQt5 import QtWidgets

class Command:
    def __init__(self, model, id):
        self.model = model
        self.id = id

    def getQTWidget(self):
        return QtWidgets.QAction(self.id, None)

    def execute(self):
        print("executing")
        # return NotImplemented()