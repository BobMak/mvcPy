
class Publisher:
    def __init__(self, subs=[]):
        self.subs = subs

    def notify(self):
        for s in self.subs:
            s.update()

    def addSubscriber(self, sub):
        self.subs.append(sub)


class Model(Publisher):
    def __init__(self):
        Publisher.__init__(self)