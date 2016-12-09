directions = 'R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, L1, L1, R1'

directionList = [item.strip() for item in directions.split(',')]

# (x, y): visited
visitedCoords = [(0,0)]
curCoord = (0,0)
# 0=N 1=E 2=S 3=W
curDir = 0

for direction in directionList:
    if direction[0] == 'R':
        # Turning right
        curDir += 1
    else:
        # Turning left
        curDir -= 1
    for i in range(1, int(direction[1:]) + 1):
        if curDir % 4 == 0:
            #north
            newCoord = (curCoord[0], curCoord[1] + 1)
        elif curDir % 4 == 1:
            #east
            newCoord = (curCoord[0] + 1, curCoord[1])
        elif curDir % 4 == 2:
            #south
            newCoord = (curCoord[0], curCoord[1] - 1)
        elif curDir % 4 == 3:
            #west
            newCoord = (curCoord[0] - 1, curCoord[1])
        if newCoord in visitedCoords:
            print(newCoord)
            print('{} blocks away'.format(abs(newCoord[0])+abs(newCoord[1])))
            raise SystemExit
        curCoord = newCoord
        visitedCoords.append(curCoord)
 
print('No location visited twice!')
