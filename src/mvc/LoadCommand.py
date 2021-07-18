from PyQt5.QtWidgets import QFileDialog

from mvc.Command import Command


class LoadCommand(Command):
    def __init__(self, model, id):
        Command.__init__(self, model, id)

    def execute(self):
        qfd = QFileDialog(None)
        options = qfd.Options()
        # options |= qfd.DontUseNativeDialog
        fileName, _ = qfd.getOpenFileName(
            None, "QFileDialog.getOpenFileName()", "",
            "All Files (*);;Python Files (*.pkl)", options=options)
        if fileName:
            print(fileName)
            self.model.load(fileName)