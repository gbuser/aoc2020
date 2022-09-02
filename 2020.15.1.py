data = [x.rstrip().split(',') for x in open('data.txt', 'r')]
data = [int(x) for x in data[0]]

numbers = {}
said_numbers = []
for x in data:
    numbers[x] = data.index(x) + 1
    said_numbers.append(x)

position = len(numbers)+1
current = 0
end = 2020
for i in range (len(numbers), end -1 ):
    if current not in numbers.keys():
        next = 0
        numbers[current] = position
        current = next

    else:
        next = position - numbers[current]
        numbers[current] = position
        current = next
    position += 1
print(current)
