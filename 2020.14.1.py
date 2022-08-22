import re
data = [x.rstrip() for x in open('data.txt', 'r')]
#memory = a dict of locations an stored values
memory = {}

#given an intruction with memory location and value, parse and convert value to a binary string with 
# 0's padded to make 36 bit and the '0b' sliced off
def parse_mem(instruction):
    mem_loc, original_value = re.findall("[0-9]+", instruction)
    original_value = (int(original_value))
    original_value = format(original_value, '#038b')[2:]
    return (mem_loc, original_value)

#merge bitmask and value. iterate through bitask and replace 'X's with the same digit from value. 
#propagate a new string and return t 
def merge(bitmask, mem_value):
    temp = str()
    bit_list = get_unmasked_bits(bitmask)
    for i in range(len(bitmask)):
        if bitmask[i] == 'X':
            temp += mem_value[i]
        else:
            temp += bitmask[i]
    return temp

#main loop: get a new bitmask or process an instruction    
for x in data:
    if re.search('mask', x) :
        bitmask = re.search("[01X]+", x).group(0)
    else:
        (mem_loc, mem_value) = parse_mem(x)
        mem_value = int(merge(bitmask, mem_value), 2)
        memory[mem_loc] = mem_value
        
total = 0
for location in memory:
    total += memory[location]
print(total)
