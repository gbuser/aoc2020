slopes = [(1,1), (3,1),(5,1),(7,1),(1,2)]

width = len(data[0])
height = len(data)

trees = []
tree_product = 1
for y in range(len(data)):
    for x in range(len(data[0])):
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

for slope in slopes:
    tree_product *= hit_trees(slope[0], slope[1], trees, width, height)
print(tree_product)
