data=[x.replace('-', ' ').replace(':', '').split() for x in open('data.txt', 'r')]

data = [[int(x[0]), int(x[1]), x[2], x[3]] for x in data]

count = 0
for x in data:
    condition1 = x[3][x[0] - 1 ] == x[2]
    condition2 = x[3][x[1] - 1 ] == x[2]
    if condition1 ^ condition2: count += 1
print(count)