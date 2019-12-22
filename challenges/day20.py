from datetime import datetime

CARDINAL_DIRS = [[0, -1], [0, 1], [-1, 0], [1, 0]]

def position(x, y): return 'c' + str(x) + 'r' + str(y)

class MazeNode(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.name = position(x, y)
    self.exits = []
    self.visited = False
    self.distance = -1
  def getInfo(self):
    return [self.name, self.x, self.y]
  def getVisited(self):
    return self.visited
  def getExits(self):
    return self.exits
  def getDistance(self):
    return self.distance
  def setExit(self, name, levelChange):
    self.exits.append([name, levelChange])
  def setDistance(self, d):
    self.visited = True
    self.distance = d
  def print(self):
    print('d=' + str(self.distance).zfill(3) + ' ... ' + self.name)

def readInputs(adjListDict, portalsDict):
  with open('./inputs/day20.txt', 'r') as f:
    row = 1
    maxRow = 1
    maxCol = 1
    while(True):
      charList = list(f.readline().rstrip('\r\n'))
      col = 0
      for c in charList:
        col += 1
        maxCol = max(maxCol, col)
        if c == '#' or c == ' ': continue

        newNode = MazeNode(col, row)
        newPos = position(col, row)
        adjListDict[newPos] = newNode
        if c == '.': continue

        if c == 'B':
          begin = newPos
        elif c == 'E':
          end = newPos
        elif c in portalsDict: 
          portalsDict[c].append(newPos)
        else:
          portalsDict[c] = [newPos]

      if not len(charList): break
      maxRow = max(maxRow, row)
      row += 1

  return [begin, end, maxCol, maxRow]

def findDistancesFromStart(adjListDict, begin):
  queue = []
  distance = 0
  level = 0

  adjListDict[begin].setDistance(distance)
  queue.append([begin, distance]) 
  
  while queue:
    (name, dist) = queue.pop(0)
    node = adjListDict[name]

    for [nextPos, levelChange] in node.getExits(): 
      nextNode = adjListDict[nextPos]
      level += levelChange
      if nextNode.getVisited() == False:
        nextNode.setDistance(dist + 1)
        queue.append([nextPos, dist + 1])

def isPortalOnOutsideEdge(pos, w, h):
  if 'c1' in pos: return True
  if 'r1' in pos: return True
  if 'c' + str(w) in pos: return True
  if 'r' + str(h) in pos: return True

#
# main
#
startTime = datetime.now()

# inputs
adjListDict = {}
portalsDict = {}
[begin, end, inputWidth, inputHeight] = readInputs(adjListDict, portalsDict)

for key in adjListDict: 
  (pos, x, y) = adjListDict[key].getInfo()
  for (dx, dy) in CARDINAL_DIRS:
    nextPosition = position(x + dx, y + dy)
    if nextPosition in adjListDict:
      adjListDict[key].setExit(nextPosition, 0)

for c in portalsDict:
  (pos1, pos2) = portalsDict[c]
  levelChangeFromPos1ToPos2 = 1
  if isPortalOnOutsideEdge(pos1, inputWidth, inputHeight):
    levelChangeFromPos1ToPos2 = -1
  adjListDict[pos1].setExit(pos2, levelChangeFromPos1ToPos2)
  adjListDict[pos2].setExit(pos1, -levelChangeFromPos1ToPos2)

findDistancesFromStart(adjListDict, begin)

# for n in adjListDict: adjListDict[n].print()
# print('begin:', begin, 'end:', end)

print('# solution:', adjListDict[end].getDistance())
print('# compute time:', str(datetime.now() - startTime)[:-3])
# solution: 620
# compute time: 0:00:00.116
