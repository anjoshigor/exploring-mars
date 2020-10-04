import logging
from model.probe import Probe
from model.land import Land
from controller.nasa import Nasa

def main(land, probe, movements):
    nasa = Nasa(land)
    for direction in movements:
        probe = nasa.move(probe, direction)

    return "{} {} {}".format(probe.x, probe.y, probe.direction)


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
            print(main(land, probe, movements))
    except EOFError:
        logging.info("End of program")