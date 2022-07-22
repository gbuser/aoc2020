data = [x.rstrip() for x in open('data.txt', 'r')]

#replace L with 0 and use 1 for # to facilitate scoring logic
data = [[(0 if x == 'L' else '.') for x in line] for line in data]

#an nonborder seat has 8 neighbors, subtract those outside the boundary for border seats
def neighbors(row, column, height, width):
    
    neighbor_list = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
    (top, bottom, left, right) = (0, height -1, 0, width -1)
    if row == top:
        neighbor_list -= {(-1, 0), (-1, -1), (-1, 1)}
    if row == bottom:
        neighbor_list -= {(1, 0), (1, -1), (1, 1)}
    if column == left:
        neighbor_list -= {(-1, -1), (1, -1), (0, -1)}
    if column == right:
        neighbor_list -= {(-1, 1), (0, 1), (1, 1)}
    return neighbor_list

def score_seat(row, column, neighbors, data):
    
    score = 0
    for (delta_row, delta_column) in neighbors:
        if data[row + delta_row][column + delta_column] == 1:
            score += 1
    return score
    
height = len(data)
width = len(data[0])

#straightforward main loop. 
#score each seat and create a list of seats that will change
#then iterate over the change list
#if change list is empty, the pattern has stabilized
while True:
    changes = set()
    for row in range(height):
        for column in range(width):
            neighbor_list = neighbors(row, column, height, width)
            score = score_seat(row, column, neighbor_list, data)

            if score == 0:
                if data[row][column] == 0:
                    changes.add((row, column))

            if score >= 4:
                if data[row][column] == 1:
                    changes.add((row, column))
    for (row, column) in changes:
        data[row][column] = (0 if data[row][column] else 1)
    
    if len(changes) == 0: break
    
#tally the answer
answer = 0
for line in data:
    for x in line:
        if x==1: answer += 1
print(answer)
