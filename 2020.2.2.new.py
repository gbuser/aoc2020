data=[x.replace('-', ' ').replace(':', '').split() for x in open('data.txt', 'r')]

data = [ { 'first': int(x[0])-1, 'second': int(x[1]) -1, 'letter': x[2], 'password' : x[3]} for x in data]

count = 0
for x in data:
    condition1 = x['password'][x['first']] == x['letter']
    condition2 = x['password'][x['second']] == x['letter']
    if condition1 ^ condition2: count += 1
print(count)
