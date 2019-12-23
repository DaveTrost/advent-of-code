from datetime import datetime

CARDINAL_DIRS = [[0, -1], [0, 1], [-1, 0], [1, 0]]
DEBUG_MODE = False

def position(x, y): return 'c' + str(x) + 'r' + str(y)

class MazeNode(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.name = position(x, y)
    self.exits = []
    self.visitsByLevel = {}
    self.distancesByLevel = {}
  def getInfo(self):
    return [self.name, self.x, self.y]
  def getVisits(self):
    return self.visitsByLevel
  def getExits(self):
    return self.exits
  def setExit(self, name, levelChange):
    self.exits.append([name, levelChange])
  def getDistances(self):
    return self.distancesByLevel
  def setDistance(self, d, level):
    self.visitsByLevel[level] = True
    self.distancesByLevel[level] = d
  def printDistances(self):
    for d in self.distancesByLevel:
      print('d=' + str(self.distancesByLevel[d]).zfill(3) + ' ... ' + self.name)

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

def findDistancesFromStart(adjListDict, begin, end):
  queue = []
  startLevel = 0
  startDistance = 0
  queue.append([begin, startDistance, startLevel])
  
  while queue:
    # pop the next node from the queue (breadth first approach) and mark it visited
    (name, dist, level) = queue.pop(0)
    node = adjListDict[name]
    node.setDistance(dist, level)

    # check the end condition
    if name == end and level == 0: return

    for [nextPos, levelChange] in node.getExits():

      # check invalid queueing conditions
      if nextPos == end and level > 0: continue
      nextLevel = level + levelChange
      if nextLevel < 0: continue

      # add the neighboring node, its level and its distance to the queue  
      nextNode = adjListDict[nextPos]
      visits = nextNode.getVisits()
      if (not nextLevel in visits) or (not visits[nextLevel]):
        queue.append([nextPos, dist + 1, nextLevel])
        if DEBUG_MODE and levelChange == 1: print(name, '-->', nextPos, nextLevel, dist + 1)
        if DEBUG_MODE and levelChange == -1: print(name, ' ^^^^ ', nextPos, nextLevel, dist + 1)

def isPortalOnOutsideEdge(pos, w, h):
  [x, y] = pos.split('c')[1].split('r')
  if x == '1' or y == '1': return True
  if x == str(w): return True
  if y == str(h): return True

def connectMazeNodesAndPortals(adjListDict, portalsDict):
  for key in adjListDict: 
    (pos, x, y) = adjListDict[key].getInfo()
    for (dx, dy) in CARDINAL_DIRS:
      nextPosition = position(x + dx, y + dy)
      if nextPosition in adjListDict:
        adjListDict[key].setExit(nextPosition, 0)
  for c in portalsDict:
    [pos1, pos2] = portalsDict[c]
    levelChangeFromPos1ToPos2 = 1
    if isPortalOnOutsideEdge(pos1, inputWidth, inputHeight):
      levelChangeFromPos1ToPos2 = -1
    adjListDict[pos1].setExit(pos2, levelChangeFromPos1ToPos2)
    adjListDict[pos2].setExit(pos1, -levelChangeFromPos1ToPos2)

#
# main
#
startTime = datetime.now()

# inputs
adjListDict = {}
portalsDict = {}
[begin, end, inputWidth, inputHeight] = readInputs(adjListDict, portalsDict)

connectMazeNodesAndPortals(adjListDict, portalsDict)

findDistancesFromStart(adjListDict, begin, end)

print('# solution:', adjListDict[end].getDistances()[0])
print('# compute time:', str(datetime.now() - startTime)[:-3])
# solution: 7366
# compute time: 0:00:16.654