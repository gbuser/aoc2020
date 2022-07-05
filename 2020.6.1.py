data =[x for x in open('data.txt', 'r')]
data = [set(x.replace('\n', '')) for x in ''.join(data).split('\n\n')]

answer = 0
for group in data:
    answer += len(group)
print(answer)
