data = [x.rstrip() for x in open('data.txt', 'r')]
keys = (('F', '0'), ('B', '1'), ('L', '0'), ('R', '1'))

max_seat_ID = 0
for seat in data:
    for key, value in keys:
        seat = seat.replace(key, value)
    seat_ID = int(seat, 2)
    if seat_ID > max_seat_ID:
        max_seat_ID = seat_ID
        
print(max_seat_ID)
