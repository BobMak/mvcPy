import pickle


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
        self.savable = []  # attributes that will be saved and loaded

    def save(self, filename):
        toSave = {}
        for attribute in self.savable:
            toSave[attribute] = self.__dict__[attribute]
        with open(filename, "wb") as f:
            pickle.dump(toSave, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        with open(filename, "rb") as f:
            saved = pickle.load(f)
        for attribute, value in saved.items():
            self.__dict__[attribute] = saved[attribute]