import userin

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'

COMPASS = [NORTH, EAST, SOUTH, WEST]
SHIPS_DIRECTION = EAST

class Ship:
    facing = EAST
    position = (0,0)

    def move(self, cmd):
        c = cmd[0]
        units = int(cmd[1:])
        if c == LEFT or c == RIGHT:
            units //= 90
            if (c == LEFT):
                units *= -1
            self.facing = COMPASS[(COMPASS.index(self.facing) + units) % 4]
            return
        elif c == FORWARD:
            c = self.facing
        moveVector = (0,0)
        if c == NORTH:
            moveVector = (0,1)
        elif c == SOUTH:
            moveVector = (0,-1)
        elif c == EAST:
            moveVector = (1,0)
        elif c == WEST:
            moveVector = (-1,0)
        self.position = [x + y * units for x, y in zip(self.position, moveVector)]


        

ship = Ship()