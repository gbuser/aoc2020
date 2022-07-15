data = [x.rstrip().split() for x in open('data.txt', 'r')]
data = [[x[0], int(x[1])] for x in data]

#takes a list of instructions and executes. returns true if ends just after last line
def run_program(data):
    lines_visited = []
    program_counter = 0
    accumulator = 0
    while program_counter in range(len(data)):
        if program_counter in lines_visited: #infinite loop
            return (False)
        if program_counter == len(data) - 1: # ended after last line = success
            print(f"accumulator = {accumulator}")
            return True
        lines_visited.append(program_counter)
        
        command, number = data[program_counter]
        if command == 'acc':
            accumulator += number
            program_counter += 1
        if command == 'nop':
            program_counter += 1
        if command == 'jmp':
            program_counter += number
    return (False) # jmp'ed out of range
    
# swap nop/jmp at specified index
def swap_nop_jmp(temp_data, index):
    if temp_data[index][0] == 'nop': 
        temp_data[index][0] = 'jmp'
    elif temp_data[index][0] == 'jmp':
        temp_data[index][0] = 'nop'
    return temp_data

nop_and_jmp = [] #a list of indices of all nop and jmps
accumulator = 0
program_counter = 0
lines_visited = set()

#populate the nop/jmp list
for i in range(len(data)):
    if data[i][0] in ('jmp', 'nop'):
        nop_and_jmp.append(i)

#main loop: ends when all nop/jmp swaps have been tried and none succeeded (shouldnt happen)
#pop an index and swap
#test the swapped program, and break if success
#undo the nop/jmp swap
while len(nop_and_jmp):
    index = nop_and_jmp.pop()
    data = swap_nop_jmp(data, index)
    if run_program(data):
        break
    data = swap_nop_jmp(data, index)
