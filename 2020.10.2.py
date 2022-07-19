data = [int(x.rstrip()) for x in open('data.txt', 'r')]
data.sort()

#add the outlet and device
data.insert(0,0)
data.append(data[-1] +3)

#threes is a list of adapters ending a 3 jolt gap, (with none in betwen) with the outlet add to start from
threes = [data[x] for x in range (1, len(data)) if (data[x] - data[x-1]) ==3 ]
threes.insert(0, 0)
 
#total_paths starts at one because each group of paths from one three to the next will be multiplied 
#to the growing total
total_paths = 1

#if there are 5 ways to get from point a to point b and 6 ways from point b to point c
#and no way to get to point c without going through point b
#then there are 30 ways to get from point a to point c
#so count the paths from each adapter in threes to the next and multiply all segments together
#pending_paths is a list of expanding paths, each path beginning at the start of a segment
#and appending points until the next three is reached. 
#Each is popped from the list when it is extended.
#completed_paths tallies the number of paths in this segment, the path themselves are not needed
#when the next three is reached, complete_paths increments

for starting_adapter in threes[:-1]:
    complete_paths = 0
    pending_paths = [[starting_adapter]]
    ending_adapter = threes[threes.index(starting_adapter) + 1 ]
    
    while pending_paths:
        
        current_path = pending_paths.pop()
        last_adapter_in_current_path = current_path[-1]
        
        if (last_adapter_in_current_path + 1) in data:
            pending_paths.append(current_path + [last_adapter_in_current_path + 1])
            

        if (last_adapter_in_current_path + 2) in data:
            pending_paths.append(current_path + [last_adapter_in_current_path + 2])
            
            
        #if a three gap exists, but there are adapters in between, the end has not been reached
        if last_adapter_in_current_path + 3 in data:
            if (last_adapter_in_current_path +3) != ending_adapter:
                pending_paths.append(current_path + [last_adapter_in_current_path + 3])
            

        #the end of this segment has been reached by this path (but all paths not yet found)
        if (last_adapter_in_current_path + 3) == ending_adapter:
            complete_paths += 1
    
    
    total_paths *= complete_paths
print(total_paths)
