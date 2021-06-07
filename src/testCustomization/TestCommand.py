from mvc.Command import Command


class TestCommand(Command):
    def __init__(self, model, id):
        Command.__init__(self, model, id)

    def execute(self):
        self.model.drawShape()