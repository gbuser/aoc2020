#code is identical to part 1 with an added w dimension. Runs a bit slowly
data = [x.rstrip() for x in open('data.txt', 'r')]

#initialize the starting range in three axes
xstart = len(data[0])
ystart = len(data)
zstart = 1
wstart = 1

generations = 6

#the "universe" has to included the starting square, a layer for every generation around it and one more 
#surrounding layer in case the last generation activates cubes in outside of that last layer (+2 cuz top/bottom, L/R, front/back)

xrange = xstart + generations * 2 + 2
yrange = ystart + generations * 2 + 2
zrange = zstart + generations * 2 + 2
wrange = wstart + generations * 2 + 2

#create a list of vectors to neigboring cubes, removing the zero vector
neighbors = []
for x in (-1, 0, 1):
    for y in (-1, 0, 1):
        for z in (-1, 0, 1):
            for w in (-1, 0, 1):
                neighbors.append((x, y, z, w))
neighbors.remove((0, 0, 0, 0))


#create a multidimensional list of "cubes", one for each set of coordinates you'll need to include. each cube is just a 0 or 1 
#representing active state
universe =[[ [[0] * wrange for z in range(zrange)] for y in range(yrange)] for x in range(xrange)]

#now create a list of coordinates to access each cube in the multidimensional list
universe_coords = []
for x in range(1, xrange - 1):
    for y in range(1, yrange - 1):
        for z in range(1, zrange - 1):
            for w in range(1, wrange - 1):
                universe_coords.append((x, y, z, w))

for x in range(xstart):
    for y in range(ystart):
        if data[x][y] == '#':
            universe[x + 7][y + 7][7][7]= 1
            


def score_volume(volume):
    score = 0
    for item in volume:
        x, y, z , w = item
        score += universe[x][y][z][w]
    return score
        

def score_coord(coord):
    score = 0
    x, y, z , w = coord
    for offset in neighbors:
        dx, dy, dz, dw = offset
        score += universe[x + dx][y + dy][z + dz][w + dw]
    return score
        

def generation(volume):
    change_list = []
    
    for coord in volume:
        x, y, z, w = coord
        
        score = score_coord((x, y, z, w))
        if universe[x][y][z][w] == 1:
            if score  not in (2, 3):
                change_list.append((x, y, z, w))
                
        else:
            if score == 3:
                change_list.append((x, y, z, w))
    for item in change_list:
        x, y, z, w = item
        universe[x][y][z][w] = universe[x][y][z][w] ^ 1


for i in range (1, 7):
    generation(universe_coords)
print(score_volume(universe_coords))
