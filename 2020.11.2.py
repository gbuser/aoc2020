data = [x.rstrip() for x in open('data.txt', 'r')]
#convert L to 0 and # to 1 to simplify scoring
data = [[(0 if x == 'L' else '.') for x in line] for line in data]

height = len(data)
width = len(data[0])
#each seat expressed as (row, column) for clarity
vectors = { 'N': (-1, 0), 'NE':(-1,1), 'E':(0, 1), 'SE': (1, 1), 'S': (1, 0), 
           'SW': (1, -1), 'W': (0, -1), 'NW': (-1, -1)}

#function to check if a seat is in bounds
def inGrid(row, column, data):
    height = len(data)
    width = len(data[0])
    
    if row < 0: return False
    if row >= height: return False
    if column < 0: return False
    if column >= width: return False
    return True
    
#gets the status of the first seat in the given direction or returns 0 if it leaves bounds first
def goDirection(row, column, vector, data):
    delta_row, delta_column = vector
    while inGrid(row + delta_row, column + delta_column, data):
        row += delta_row
        column += delta_column
        if data[row][column] != '.':
            return data[row][column]
    return 0
        
#go in each direction and total the score
def scoreSeat(row, column, data):
    score = 0
    for vector  in vectors.values():
        score += goDirection(row, column, vector, data)
    return score

#main loop. keep a list of seats that flip. stop when no seats flip. then flip the seats from the list
while True:
    changeList = []
    for row in range(height):
        for column in range(width):
            if data[row][column] == '.' : continue
            score = scoreSeat(row, column, data)
            if data[row][column] == 0 and score == 0:
                changeList.append((row, column))
            if data[row][column] == 1 and score > 4:
                changeList.append((row, column))
    if  not changeList: break


    for seat in changeList:
        row, column = seat
        data[row][column] = (-1 * data[row][column]) + 1

#lastly, count occupied seats        
result = 0
for row in range(len(data)):
    for column in range(len(data[0])):
        if data[row][column] == 1:
            result += 1
print(result)
