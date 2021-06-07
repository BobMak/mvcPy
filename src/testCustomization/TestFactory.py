from TestModel import TestModel
from TestView import TestView
from TestCommand import TestCommand
from mvc.Factory import Factory


class TestFactory(Factory):
    @staticmethod
    def makeModel():
        return TestModel()

    @staticmethod
    def makeView(model):
        return TestView(model)

    @staticmethod
    def getToolBarCommands():
        return ["generate circle"]

    @staticmethod
    def makeCommand(model, commandStr):
        return TestCommand(model, commandStr)

    @staticmethod
    def makeHelp():
        return "default help"