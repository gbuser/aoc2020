data = [ x.rstrip() for x in open('data.txt', 'r')]
data = [(x[0], int(x[1:])) for x in data]

directions = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
move_vectors = {0: (0, -1), 90: (1, 0), 180: (0, 1), 270: (-1, 0)}

class Ship:
    xpos = 0
    ypos = 0
    pointing = 90
    
    def move(self, waypoint, scalar):
        #vector from ship to waypoint
        x_vector = waypoint.xpos - self.xpos
        y_vector = waypoint.ypos - self.ypos
        
        self.xpos += (scalar * x_vector)
        self.ypos += (scalar * y_vector)
        
        #reset the waypoint
        waypoint.xpos = self.xpos + x_vector
        waypoint.ypos = self.ypos + y_vector
        
    
class Waypoint:
    xpos = 10
    ypos = -1
    
    def rotate(self, ship, instruction):
        direction, degrees = instruction
        which_way = (-1 if direction == 'L' else 1)
        rotation = (which_way * degrees) % 360
        x_vector = self.xpos - ship.xpos
        y_vector = self.ypos - ship.ypos
        
        if rotation == 90:
            self.xpos = ship.xpos - y_vector
            self.ypos = ship.ypos + x_vector
        if rotation == 180:
            self.xpos = ship.xpos - x_vector
            self.ypos = ship.ypos - y_vector
        if rotation == 270:
            self.xpos = ship.xpos + y_vector
            self.ypos = ship.ypos - x_vector
            
    def move(self, direction, scalar):
        self.xpos += (scalar * move_vectors[directions[direction]][0])
        self.ypos += (scalar * move_vectors[directions[direction]][1])
        
ship = Ship()
waypoint = Waypoint()

for (direction, scalar) in data:
    if direction in ('N', 'S', 'E', 'W'):
        waypoint.move(direction, scalar)
    if direction in ('L', 'R'):
        waypoint.rotate(ship, (direction, scalar))
    if direction == 'F':
        ship.move(waypoint, scalar)

ship.xpos +ship.ypos
