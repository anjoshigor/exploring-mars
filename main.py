
class Matrix(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Nasa(object):
    def moveLeft(self, drone):
        drone.direction = self.left[drone.direction]
        return drone

    def moveRight(self, drone):
        drone.direction = self.right[drone.direction]
        return drone

    def moveForward(self, drone):
        return self.forward[drone.direction](drone)

    def __init__(self):
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
            "N": lambda drone: Drone(drone.x, drone.y+1, drone.direction),
            "E": lambda drone: Drone(drone.x+1, drone.y, drone.direction),
            "W": lambda drone: Drone(drone.x-1, drone.y, drone.direction),
            "S": lambda drone: Drone(drone.x, drone.y-1, drone.direction)
        }

    def move(self, drone, direction):
        return self.movements[direction](drone)



class Drone(object):    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


if __name__ == "__main__":
    matrixInput = input()
    indexes = matrixInput.split(" ")
    
    matrix = Matrix(indexes[0], indexes[1])

    try:
        while True:
            droneLocation = input()
            location = droneLocation.split(" ")
            drone = Drone(int(location[0]), int(location[1]), location[2])
            movements = input()
            nasa = Nasa()
            for direction in movements:
                drone = nasa.move(drone, direction)

            print(drone.x, drone.y, drone.direction)
    except EOFError:
        print("End of program")