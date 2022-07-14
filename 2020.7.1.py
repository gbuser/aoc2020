import re
data = [x.rstrip() for x in open('data.txt', 'r')]

#split line into list at each digit char
data = [re.split('[0-9]', x) for x in data]

#split split each item of each lines list into individual words
data = [[x.split() for x in line ] for line in data]

#keep the first two words (e.g. 'dim', 'yellow') and concatenate 
data =[[x[0] + ' ' + x[1] for x in line] for line in data]

#make rules dict where key= a bag and value is a list of bags it contains
rules = {}
for rule in data:
    rules[rule[0]] = []
    for item in rule:
        #don't include the bag in its own values
        if item != rule[0]: rules[rule[0]].append(item)
            
#an expanding set of bags that contain bags that ultimate contain a shiny gold bag
#bags get removed after we've appended all their parents
unprocessed_parents = set() 

#start the set
for key in rules:
    if 'shiny gold' in rules[key]:
        unprocessed_parents.add(key)

#bags go here after we've appended their parents
        completed = set()

#main loop: so long as there are unprocessed parents- 
#pop a bag, add its parents to unprocessed if not in the completed set
#add the bag to completed set
while len(unprocessed_parents):
    bag = unprocessed_parents.pop()
    for key in rules:
        if bag in rules[key]:
            if key not in completed:
                unprocessed_parents.add(key)
    completed.add(bag)
    
print(len(completed))
