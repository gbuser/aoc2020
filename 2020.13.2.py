data =[x.rstrip()for x in open('data.txt', 'r')][1].split(',')

buses = []
#each bus is a tuple wqith (period, minutes to arrive after timestamp - ie "wait")
for i in range(len(data)):
    if data[i] != 'x':
        buses.append((int(data[i]), i % int(data[i])))

#candidates are possible timestamps that satisfy each condition. given the lowest candidate that satisfies conditions 
#thus far, find the smallest that satisfies the next condition. 
# as conditions are added, the next timestamp will have to be the current timestamp plus a multiple of the 
#product of all the periods so far. 
# the bus you missed arrived timestamp % period minutes ago (remainder), the next arrives one period later
# wait = how long you have to wait from timestamp (candidate) to  the next bus. wait + remainder = period

def get_next_candidate(candidate, product, bus):
    (period, wait) = bus
    
    remainder = period - wait
    while True:
        candidate += product
        if candidate % period == remainder:
            return candidate, product
        
    

candidate = buses[0][0]
#product is multiplied by each successive period as the condition is added. When finding the next timestamp that meets all
#current conditions, it must be greater than the current timestamp by a multiple of the product. evaluate each one until 
# the next condition is satisfied
product = buses[0][0]

for i in range(1, len(buses)):
    candidate, product = get_next_candidate(candidate, product, buses[i])
    product *= buses[i][0]

print(candidate)
