data = [x.rstrip() for x in open('data.txt', 'r')]
keys = (('F', '0'), ('B', '1'), ('L', '0'), ('R', '1'))

seats = []
for seat in data:
    for key, value in keys:
        seat = seat.replace(key, value)
    seats.append(int(seat, 2))
    
missing_seats = [x for x in range(len(seats)) if x not in seats]

print([x for x in missing_seats if (x-1)not in missing_seats and (x+1) not in missing_seats])
