class Probe(object):    
    def __init__(self, x=0, y=0, direction="N"):
        self.x = x
        self.y = y
        self.direction = direction

    def __str__(self):
        return "[{x}, {y}, {d}]".format(x=self.x, y=self.y, d=self.direction)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.direction == other.direction