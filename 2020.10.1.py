data = [int(x.rstrip()) for x in open('data.txt', 'r')]
data.sort()

data.insert(0,0) #start at the outlet (0)
data.append(data[-1] +3) #end at the device (+3 from last adapter)
ones = 0
threes = 0

for i in range(len(data) - 1):
    diff = data[i + 1] - data[i]
    if diff == 1: ones += 1
    if diff == 3: threes += 1

print(ones * threes)
