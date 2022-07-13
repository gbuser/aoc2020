data =[x.rstrip() for x in open('data.txt', 'r')]

groups = []
group = []
answer = 0

#parse data into a list of groups, each group a list of sets, each set is one person
for line in data:
    if len(line):
        group.append(set(line))
    else:
        groups.append(group)
        group = []
groups.append(group)
    
    

#in each group, intersect each persons choices, only those in all sets remain
for group in groups:
    everybody = group[0]
    for item in group:
        everybody = everybody.intersection(item)
    answer += len(everybody)
print (answer)
