from model.probe import Probe
from model.land import Land
from helpers.validator import Validator

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