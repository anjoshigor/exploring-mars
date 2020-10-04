import logging

class Land(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Validator(object):

    @staticmethod
    def validateBoundaries(probe, land):
        if(probe.x > land.x or probe.y > land.y or probe.x < 0 or probe.y < 0):
            logging.warning("Probe with postion {} is trying to go out Mars land".format(probe))
            return False

        return True

    @staticmethod
    def validate(probe, land):
        functions = [Validator.validateBoundaries]
        for func in functions:
            if(not func(probe, land)):
                return False
        return True

class Nasa(object):

    def moveLeft(self, probe):
        probe.direction = self.left[probe.direction]
        return probe

    def moveRight(self, probe):
        probe.direction = self.right[probe.direction]
        return probe

    def moveForward(self, probe):
        movedProbe = self.forward[probe.direction](probe)
        if(not Validator.validate(movedProbe, self.land)):
            return probe

        return movedProbe

    def __init__(self, land):
        self.land = land
        self.movements = {
            "L": self.moveLeft,
            "R": self.moveRight,
            "M": self.moveForward
        }
        self.left = {
            "N": "W",
            "E": "N",
            "W": "S",
            "S": "E"
        }
        self.right = {
            "N": "E",
            "E": "S",
            "W": "N",
            "S": "W"
        }
        self.forward = {
            "N": lambda probe: Probe(probe.x, probe.y+1, probe.direction),
            "E": lambda probe: Probe(probe.x+1, probe.y, probe.direction),
            "W": lambda probe: Probe(probe.x-1, probe.y, probe.direction),
            "S": lambda probe: Probe(probe.x, probe.y-1, probe.direction)
        }

    def move(self, probe, direction):
        return self.movements[direction](probe)



class Probe(object):    
    def __init__(self, x=0, y=0, direction="N"):
        self.x = x
        self.y = y
        self.direction = direction

    def __str__(self):
        return "[{x}, {y}, {d}]".format(x=self.x, y=self.y, d=self.direction)


if __name__ == "__main__":
    landInput = input()
    indexes = landInput.split(" ")
    
    land = Land(int(indexes[0]), int(indexes[1]))

    try:
        while True:
            probeLocation = input()
            location = probeLocation.split(" ")
            probe = Probe(int(location[0]), int(location[1]), location[2])
            movements = input()
            nasa = Nasa(land)
            for direction in movements:
                probe = nasa.move(probe, direction)

            print(probe.x, probe.y, probe.direction)
    except EOFError:
        logging.info("End of program")