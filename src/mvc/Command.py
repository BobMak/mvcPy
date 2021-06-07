class Command:
    def __init__(self, model, id):
        self.model = model

    def trigger(self):
        print("executing")
        # return NotImplemented()