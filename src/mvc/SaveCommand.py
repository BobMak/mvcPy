from PyQt5.QtWidgets import QFileDialog

from mvc.Command import Command


class SaveCommand(Command):
    def __init__(self, model, id):
        Command.__init__(self, model, id)

    def execute(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            None, "QFileDialog.getSaveFileName()", "",
            "All Files (*);;All Files (*.pkl)", options=options
        )
        if fileName:
            print(fileName)
            self.model.save(fileName)