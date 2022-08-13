data = [x.rstrip() for x in open('data.txt', 'r')]
start_time = int(data[0])
buses = data[1].split(',')
buses = [int(y) for y in buses if y!= 'x']

#arbitrary number higher than the longest possible wait time
wait_time = 500
for bus in buses:
    #wait = the bus time minus the remainder from the bus you just missed
    bus_wait = bus - (start_time % bus)
    if bus_wait < wait_time :
        best_bus = bus
        wait_time = bus_wait
print(best_bus, wait_time, best_bus * wait_time)
