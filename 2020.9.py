#combined parts 1 and 2:
data = [int(x.rstrip()) for x in open('data.txt', 'r')]

#list the sum of each number with all that come after (through 25th number)
def make_all_sums(data):
    all_sums = []
    for i in range(len(data)-1):
        for j in range(i +1, len(data)):
            all_sums.append(data[i] + data[j] )
    return all_sums

found = False
while found == False:
    if data[25] not in make_all_sums(data[:25]):
        found = True
    data.pop(0)

result = data[24]
print(f"answer to part 1: {result}") 
###################
#now reset data and do part 2:
data = [int(x.rstrip()) for x in open('data.txt', 'r')]

found = False
for i in range(len(data)):
    sum = 0
    counter = i
    while sum < result:
        sum += data[counter]
        if sum == result:
            maximum = max(data[i : counter + 1])
            minimum = min(data[i : counter + 1])
            print("answer to part 2: ", (maximum + minimum))
            found = True
            break
        counter += 1
    if found : break
