class Command:
    def __init__(self, model, id):
        self.model = model

    def execute(self):
        print("executing")
        # return NotImplemented()