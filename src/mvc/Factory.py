from mvc.Model import Model
from mvc.View import View
from mvc.Command import Command


class Factory:
    @staticmethod
    def makeModel():
        return Model()

    @staticmethod
    def makeView(model):
        return View(model)

    @staticmethod
    def getEditCommands():
        return ["edit1", "edit2"]

    @staticmethod
    def getToolBarCommands():
        return ["toolbar1", "toolbar2"]

    @staticmethod
    def makeCommand(model, commandStr):
        # if commandStr=="undo":
        #     return UndoCommand(model)
        return Command(model, commandStr)

    @staticmethod
    def makeHelp():
        return "default help"