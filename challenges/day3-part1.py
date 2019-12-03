with open('./inputs/day3.txt', 'r') as f:
  directionsForWire1 = f.readline().split(',')
  directionsForWire2 = f.readline().split(',')

def coordinateAddition(a1, a2):
  (x1, y1) = a1
  (x2, y2) = a2
  return [x1 + x2, y1 + y2]

# def cToStr(coord):
#   (x, y) = coord
#   return str(x) + ',' + str(y)

def listOfCoordsCrossed(current, instruction):
  (x, y) = current

  (dir, *dist) = list(instruction)
  distance = int(''.join(dist))

  offsetDict = {
    'R': [1, 0],
    'L': [-1, 0],
    'D': [0, -1],
    'U': [0, 1]
  }
  (dx, dy) = offsetDict[dir]

  coords = [[x, y]]
  for i in range(distance):
    (x, y) = [x + dx, y + dy]
    coords.append([x, y])

  # modify the contents of current in-place
  current[0] = x
  current[1] = y
  return coords

# main
current = [0, 0]
coordinatesWire1 = []
for instruction in directionsForWire1:
  coordinatesWire1 += listOfCoordsCrossed(current, instruction)

current = [0, 0]
coordinatesWire2 = []
for instruction in directionsForWire2:
  coordinatesWire2 += listOfCoordsCrossed(current, instruction)

crossingPoints = []
min = 999999
for coord1 in coordinatesWire1:
  (x1, y1) = coord1
  for coord2 in coordinatesWire2:
    (x2, y2) = coord2
    if(x1 == x2 and y1 == y2):
      crossingPoints.append(coord1)
      manhattanDist = abs(x1) + abs(y1)
      if(manhattanDist < min and manhattanDist > 0): 
        min = manhattanDist
        print('new min', min, ' at ', coord1, coord2)

print(crossingPoints)
print(min)
