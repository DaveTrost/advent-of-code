with open('./inputs/day3.txt', 'r') as f:
  instructionsForWire1 = f.readline().split(',')
  instructionsForWire2 = f.readline().split(',')

def getCoordsAndOffsets(instructions):
  coordsList = []
  (x, y) = [0, 0]

  for instruction in instructions:
    (dir, *dist) = list(instruction)  # convert string to list performs a split on every character
    distance = int(''.join(dist))

    if dir == 'R': offset = [distance, 0]
    if dir == 'L': offset = [-distance, 0]
    if dir == 'U': offset = [0, distance]
    if dir == 'D': offset = [0, -distance]
    x += offset[0]
    y += offset[1]

    coordsList.append({
      'coord': [x, y],
      'offset': offset,
    })

  return coordsList

# main
coordsWire1 = getCoordsAndOffsets(instructionsForWire1)
coordsWire2 = getCoordsAndOffsets(instructionsForWire2)

crossingPoints = []
min = 999999
for coord1 in coordsWire1:
  (x1, y1) = coord1['coord']
  (dx1, dy1) = coord1['offset']
  for coord2 in coordsWire2:
    (x2, y2) = coord2['coord']
    (dx2, dy2) = coord2['offset']

    if(bool(x1 - x2 > 0) != bool(x1 - dx1 - x2 > 0)):
      if(bool(y2 - y1 > 0) != bool(y2 - dy2 - y1 > 0)):
        print('crossing x: ', coord1, coord2)

        crossingPoints.append([x2, y1])
        manhattanDist = abs(x2) + abs(y1)
        if(manhattanDist < min and manhattanDist > 0): 
          min = manhattanDist
          print('new min', min, ' at ', x2, y1)
    
    if(bool(y1 - y2 > 0) != bool(y1 - dy1 - y2 > 0)):
      if(bool(x2 - x1 > 0) != bool(x2 - dx2 - x1 > 0)):
        print('crossing y: ', coord1, coord2)

        crossingPoints.append([x1, y2])
        manhattanDist = abs(x1) + abs(y2)
        if(manhattanDist < min and manhattanDist > 0): 
          min = manhattanDist
          print('new min', min, ' at ', x1, y2)

print(crossingPoints)
print(min)
