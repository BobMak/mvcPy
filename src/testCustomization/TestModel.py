import random as rnd

from mvc.Model import Model


class TestModel(Model):
    def __init__(self):
        Model.__init__(self)
        self.shapes = []

    def drawShape(self):
        x = rnd.randint(0, 800)
        y = rnd.randint(0, 500)
        r = rnd.randint(5, 70)
        self.shapes.append((x,y,r))
        self.notify()