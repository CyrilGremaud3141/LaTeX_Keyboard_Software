import pickle

class Moin:
    def __init__(self, abc):
        self.test = abc
    
    def run(self):
        print(self.test)

a = Moin("moinsen")
a.run()


with open("test.obj", "wb") as f:
    pickle.dump(a, f)

with open("test.obj", "rb") as f:
    b = pickle.load(f)

b.run()