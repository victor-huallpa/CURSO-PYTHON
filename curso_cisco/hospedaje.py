rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
#hbitaicones por piso
# for i in range(len(rooms[0][0])):
    
#     print(i, rooms[0][0][i])
rooms[1][9][13] = True
#habitaciones por eidifio

for i in range(len(rooms)):
    
    print(i, rooms[i])
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
print(vacancy)
