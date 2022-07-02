data = [x.rstrip() for x in open('data.txt', 'r')]
(posX, posY) = (0,0)
(dx, dy) = (3, 1)
trees_hit = 0
width = len(data[0])
height = len(data)

trees = []
for y in range(height):
    for x in range(width):
        if data[y][x] == '#':
            trees.append((x,y))

while posY < height:
    posX += dx
    posY += dy
    if posX >= width:
        posX -= width
    if (posX, posY) in trees:
        trees_hit += 1
print(trees_hit)
