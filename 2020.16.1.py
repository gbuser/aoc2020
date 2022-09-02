import re
data = [x.rstrip() for x in open('data.txt', 'r')]

fields = [x for x in data if re.search("[a-z\s]+:\s\d", x)]
tickets = [x for x in data if re.search("^\d", x)]
my_ticket = tickets.pop(0)

tickets = [[int(x) for x in y.split(',') ] for  y in tickets]

ranges = [re.findall("[0-9]+", x) for x in fields]

ranges = [[int(x) for x in y] for y in ranges]

good_numbers = set()
for line in ranges:
    
    first =(set(range(line[0], line[1] + 1)))
    second =(set(range(line[2], line[3] + 1)))
    good_numbers= good_numbers.union(first.union(second))


bad = 0
for ticket in tickets:
    for number in ticket:
        if number not in good_numbers:
            bad += number
print bad
