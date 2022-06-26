rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

vacancy = 0
for hotel in range(3):
    for floor_no in range(15):
        for room_number in range(20):
            if not rooms[2][14][room_number]:
                vacancy += 1
print("No of vacant rooms :", vacancy)
