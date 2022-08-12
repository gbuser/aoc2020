data = [ x.rstrip() for x in open('data.txt', 'r')]

data = [(x[0], int(x[1:])) for x in data]

directions = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
move_vectors = {0: (0, -1), 90: (1, 0), 180: (0, 1), 270: (-1, 0)}

class Ship:
    xpos = 0
    ypos = 0
    pointing = 90
    
    # turn left or right degrees
    def rotate(self, which_way, angle):
        which_way = (-1 if which_way == 'L' else 1)
        self.pointing = (self.pointing + (which_way * angle))% 360
        
    #move in pointing direction if 'F', else in direction given    
    def move(self, direction, scalar):
        if direction == 'F':
            self.xpos += (scalar * move_vectors[self.pointing][0])
            self.ypos += (scalar * move_vectors[self.pointing][1])
        else: 
            self.xpos += (scalar * move_vectors[directions[direction]][0])
            self.ypos += (scalar * move_vectors[directions[direction]][1])
            
    def process_instruction(self, instruction):
        command, scalar = instruction
        if command in ('L', 'R'):
            self.rotate(command, scalar)
        else:
            self.move(command, scalar)
        

ship = Ship()

for instruction in data:
    ship.process_instruction(instruction)

print(ship.xpos + ship.ypos)
