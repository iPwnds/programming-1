
class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def lower(self):
        return self.lower

    def upper(self):
        return self.upper

    def is_empty(self):
        if self.lower > self.upper:
            return True
        else:
            return False

    def contains(self, value):
        if value >= self.lower and value <= self.upper:
            return True
        else:
            return False

    def overlaps_with(self, other):
        if other.is_empty() or self.is_empty():
            return False
        elif other.contains(self.upper) or other.contains(self.lower):
            return True
        elif self.contains(other.upper) or self.contains(other.lower):
            return True
        else:
            return False
