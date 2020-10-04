class Land(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "\n|{y} {y}|\n|0 {x}|".format(x=self.x, y=self.y)