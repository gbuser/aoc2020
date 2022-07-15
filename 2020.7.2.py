import re
data = [x.rstrip() for x in open('data.txt', 'r')]

#keys will be first two words of each line
key_regex = '[a-z]+ [a-z]+'

#values are a list of every occurrence of a digit followed by two words
value_regex = '[0-9] [a-z]+ [a-z]+'

#creates a dictionary of dictionaries. each bag is a key, 
#value is a dictionary where keys are contained bag and values are how many
rules = {}
for line in data:
    
    #returns the first occurrence of two words, the key
    key = (re.search(key_regex, line).group(0))
    
    # finds list of value pattern matches, splits each item into digit and bag
    values = [x.split(' ', 1) for x in re.findall(value_regex, line)]
    
    #key for each inner bag, value is how many
    values = {x[1]: int(x[0]) for x in values}
    
    rules[key] = values

total_bags = 0
untallied_bags = [('shiny gold', 1)]

#main loop: pop a bag and how many from the untallied_bags
#increment total_bags by how many bags are in DIRECTLY in this bag
#add every inner bag and how many of them to the untallied_bags
while len(untallied_bags):
    (current_bag, number_bags) = untallied_bags.pop()
    total_bags += (sum(rules[current_bag].values()) * number_bags)
    for key in rules[current_bag]:
        untallied_bags.append((key, rules[current_bag][key] * number_bags))
    
print(total_bags)
