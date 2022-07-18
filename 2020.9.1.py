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
print(data[24])
