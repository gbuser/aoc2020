data = [x.rstrip() for x in open('data.txt', 'r')]

trees = []
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '#':
            trees.append((x,y))

(posX, posY) = (0,0)
(dx, dy) = (3, 1)
trees_hit = 0
width = len(data[0])
height = len(data)

while posY < height:
    posX += dx
    posY += dy
    if posX >= width:
        posX -= width
    if (posX, posY) in trees:
        trees_hit += 1
print(trees_hit)
