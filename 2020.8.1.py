data = [x.rstrip().split() for x in open('data.txt', 'r')]
data = [[x[0], int(x[1])] for x in data]

accumulator = 0
program_counter = 0
lines_visited = set()


while program_counter not in lines_visited:
    command, number = data[program_counter]
    lines_visited.add(program_counter)
    if command == 'acc':
        accumulator += number
        program_counter += 1
    if command == 'nop':
        program_counter += 1
    if command == 'jmp':
        program_counter += number
    
print (accumulator)
