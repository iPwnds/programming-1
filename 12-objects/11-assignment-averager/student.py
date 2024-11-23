
class Averager:
    def __init__(self):
        self.value = 0
        self.i = 0

    def add(self, value):
        self.value += value
        self.i += 1

    def average(self):
        return self.value / self.i

    def reset(self):
        self.value = 0
        self.i = 0