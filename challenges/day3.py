import sys
from datetime import datetime
startTime = datetime.now()

def readInstruction(instruction):
  (dir, *rest) = list(instruction)  # list constructor from a string splits every character
  distance = int(''.join(rest))
  if dir == 'R': return [distance, 0, distance]
  if dir == 'L': return [-distance, 0, distance]
  if dir == 'U': return [0, distance, distance]
  if dir == 'D': return [0, -distance, distance]

def getPathDetails(instructions):
  coordsList = []
  x = y = 0
  distanceTraveled = 0

  for instruction in instructions:
    (dx, dy, distance) = readInstruction(instruction)
    x += dx
    y += dy
    distanceTraveled += distance
    coordsList.append({
      'coord': [x, y],
      'offset': [dx, dy],
      'distance': distanceTraveled,
    })
  return coordsList

def getCrossingPoints(coordsWire1, coordsWire2):
  crossingPoints = []

  for coord1 in coordsWire1:
    (x1, y1) = coord1['coord']
    (dx1, dy1) = coord1['offset']
    for coord2 in coordsWire2:
      (x2, y2) = coord2['coord']
      (dx2, dy2) = coord2['offset']

      if(bool(x1 - x2 > 0) != bool(x1 - dx1 - x2 > 0)):
        if(bool(y2 - y1 > 0) != bool(y2 - dy2 - y1 > 0)):
          wire1Distance = coord1['distance'] - abs(x1 - x2)
          wire2Distance = coord2['distance'] - abs(y2 - y1)
          crossingPoints.append([x2, y1, wire1Distance + wire2Distance])
      if(bool(y1 - y2 > 0) != bool(y1 - dy1 - y2 > 0)):
        if(bool(x2 - x1 > 0) != bool(x2 - dx2 - x1 > 0)):
          wire1Distance = coord1['distance'] - abs(y1 - y2)
          wire2Distance = coord2['distance'] - abs(x2 - x1)
          crossingPoints.append([x1, y2, wire1Distance + wire2Distance])

  return crossingPoints

def getMinDistance(crossingPoints):
  min = sys.maxsize
  for (x, y, d) in crossingPoints:
    if(x > 0 and y > 0 and d < min): min = d
  return min    

#
# main
#
with open('./inputs/day3.txt', 'r') as f:
  instructionsForWire1 = f.readline().split(',')
  instructionsForWire2 = f.readline().split(',')

coordsWire1 = getPathDetails(instructionsForWire1)
coordsWire2 = getPathDetails(instructionsForWire2)

crossingPoints = getCrossingPoints(coordsWire1, coordsWire2)
minDistance = getMinDistance(crossingPoints)

print('solution:', minDistance)
print('compute time:', str(datetime.now() - startTime)[:-3])
