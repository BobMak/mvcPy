from mvc.LoadCommand import LoadCommand
from mvc.Model import Model
from mvc.SaveCommand import SaveCommand
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
        return ["save", "load"]

    @staticmethod
    def getToolBarCommands():
        return []

    @staticmethod
    def makeCommand(model, commandStr):
        if commandStr=="save":
            return SaveCommand(model, None)
        if commandStr == "load":
            return LoadCommand(model, None)
        return Command(model, commandStr)

    @staticmethod
    def makeHelp():
        return "default help"