import re

#parse the data. Field lines start with letters, ticket lines with numbers
#make ticket strings into a list of ints
data = [x.rstrip() for x in open('data.txt', 'r')]

fields = [x for x in data if re.search("[a-z\s]+:\s\d", x)]
tickets = [x for x in data if re.search("^\d", x)]
tickets = [[int(x) for x in y.split(',') ] for  y in tickets]

#pull my ticket out (its the first ticket)
my_ticket = tickets.pop(0)

#parse fields into the four numberstrings that bound each of two ranges and convert to ints
ranges = [re.findall("[0-9]+", x) for x in fields]
ranges = [[int(x) for x in y] for y in ranges]

#establish a set of numbers which consists of all the ranges combined
good_numbers = set()
for line in ranges:
    first =(set(range(line[0], line[1] + 1)))
    second =(set(range(line[2], line[3] + 1)))
    good_numbers= good_numbers.union(first.union(second))

#keep only the tickets where all numbers are valid
tickets =[x for x in tickets if set(x).issubset(good_numbers)]

#this sort of duplicates a step above, left over from part 1. 
#here, the list of fields is split into the field name and its set of valid numbers
fields = [x.split(':') for x in fields]
fields = [[x[0], re.findall("[0-9]+", x[1])] for x in fields]
fields = [[x[0], [int(y) for y in x[1]]] for x in fields]

#takes a list of 4 ints and returns a set of the valid numbers including both ranges
def get_range(boundaries):
    
    first_range = set(range(boundaries[0], boundaries[1]+1))
    second_range = set(range(boundaries[2], boundaries[3]+1))
    return first_range.union(second_range)

#create a dict of field name and valid numbers
field_ranges = {}
for item in fields:
    field_ranges[item[0]] = get_range(item[1])

#create a list of sets each containing all the numbers from each ticket in a given position
#this is a bit ugly since used a dict for the field ranges.
ticket_fields = [] 
for i in range(len(tickets[0])):
       ticket_fields.append(set([ticket[i] for ticket in tickets]))

#and now a dict of which fields each postion is valid for. 
ticket_dict = {}
for i in range(20):
    ticket_dict[i] = []

for key in ticket_dict:
    for item_name in field_ranges:
        if ticket_fields[key].issubset(field_ranges[item_name]):
            ticket_dict[key].append(item_name)
            
#ticket_dict now holds a list of the 20 postions and which fields they are valid for
#it turns out, there is one position which works for a single field, one that works for this 
#field and one other, and so on, adding a new valid field to one of the remaining positions

    
#so now work backwards- find the position that works for only one field, add that to the final list
#remove that field  from all lists and repeat
final_list = []
while len(final_list) < 20:
    for key, value in ticket_dict.items():
        if len(value) == 1:
            final_list.append((key, value[0]))
            latest_field = value[0]
            for keys, item in ticket_dict.items():
                if latest_field in item:
                    item.remove(latest_field)
    
#now we needs just the fields including the word "departure"
#get there values from my ticket and multiply them
departure_list = [x for x in final_list if re.search('departure', x[1])]
answer = 1
for x in departure_list:
    answer *= my_ticket[x[0]]
print(answer)
