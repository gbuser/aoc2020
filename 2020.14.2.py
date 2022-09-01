import re
data = [x.rstrip() for x in open('data.txt', 'r')]

memory = {} #key = memory address, value = value

#data is either a new bitmask line or a memory instruction line 

#gets mem instrution line and returns mem_loc as string, value as int
def parse_mem(instruction):
    mem_loc, original_value = re.findall("[0-9]+", instruction)
    original_value = (int(original_value))
    mem_loc = (int(mem_loc))
    mem_loc = format(mem_loc, '#038b')[2:]
    return (mem_loc, original_value)
   

#takes the current bitmask and memory location and generates all memory addresses per rules
#will return a list of addresses  as ints which is 2**(number of X's in bitmask) long
def get_all_locs(bitmask, mem_loc):
    stack = ['']
    completed = []
    while len(stack):
        new_strings = get_next_segs(bitmask, mem_loc, stack.pop(0))
        for item in new_strings:
            if len(item) == 36:
                completed.append(int(item, 2))
            else:
                stack.append(item)
    return completed
    
    
#takes the current bitmask and memory location and the string stem so far. 
#processes 0 and 1 s in bitmask until an X is reached then creates two strings, ending in 0 and 1
#two incomplete strings are returned unless the string reaches length 36 
#where only that one now complete string is returned
def get_next_segs(bitmask, mem_loc, loc_so_far):
    pos= len(loc_so_far)
    two_strings = []
    while bitmask[pos] != 'X':
        if bitmask[pos] == '0':
                loc_so_far += mem_loc[pos]
        if bitmask[pos] == '1':
                loc_so_far += '1'
        if len(loc_so_far) == 36:
            return [loc_so_far]
        pos += 1
    two_strings.append(loc_so_far + '0')
    two_strings.append(loc_so_far + '1')
    return two_strings
    
#main loop: if line is bitmask, updates. if instruction, gets all memory addresses and inserts value    
for x in data:
    if re.search('mask', x) :
        bitmask = re.search("[01X]+", x).group(0)
    else:
        (mem_loc, mem_value) = parse_mem(x)
        for address in get_all_locs(bitmask, mem_loc):
            memory[address] = mem_value
        
total = 0
for location in memory:
    total += memory[location]
print(total)
