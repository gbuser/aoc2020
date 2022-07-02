data = [x.rstrip() for x in open('data.txt', 'r')]
slopes = [(1,1), (3,1),(5,1),(7,1),(1,2)]

width = len(data[0])
height = len(data)

trees = []
tree_product = 1
for y in range(height)):
    for x in range(width):
        if data[y][x] == '#':
            trees.append((x,y))

def hit_trees(dx, dy, trees, width, height):
    trees_hit = 0
    (posX, posY) = (0,0)
    while posY < height:
        posX += dx
        posY += dy
        if posX >= width:
            posX -= width
        if (posX, posY) in trees:
            trees_hit += 1
    return(trees_hit)

for (dx, dy) in slopes:
    tree_product *= hit_trees(dx, dy, trees, width, height)
print(tree_product)
