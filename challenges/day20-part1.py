import math
import sys
from datetime import datetime

DIRECTIONS_DICT = {
  'up': [0, -1],
  'down': [0, 1],
  'left': [-1, 0],
  'right': [1, 0],  
}

class MazeNode(object):
  def __init__(self, x, y, name):
    self.x = x
    self.y = y
    self.name = name
    self.exits = []
    self.visited = False
    self.distance = -1

  def getInfo(self):
    return [self.name, self.x, self.y]
  def isVisited(self):
    return self.visited
  def getExits(self):
    return self.exits
  def getDistance(self):
    return self.distance

  def addExit(self, name):
    self.exits.append(name)

  def markDistance(self, d):
    self.visited = True
    self.distance = d

  def print(self):
    print('d=' + str(self.distance).zfill(3) + ' ... ' + self.name)


def setDistanceFromStart(adjListDict, begin):
  queue = []
  distance = 0

  # Mark the source node as visited and enqueue it
  adjListDict[begin].markDistance(distance)
  queue.append([begin, distance]) 
  
  while queue:
  
    # Dequeue a vertex from queue and print it 
    (name, dist) = queue.pop(0)
    node = adjListDict[name]
  
    # Get all adjacent neighbors of the dequeued node.
    # If an adjacent has not been visited, then mark it visited and enqueue it 
    for next in node.getExits(): 
      nextNode = adjListDict[next]
      if nextNode.isVisited() == False: 
          nextNode.markDistance(dist + 1)
          queue.append([next, dist + 1])


#
# main
#
startTime = datetime.now()

adjListDict = {}
portalsDict = {}

# inputs
with open('./inputs/day20.txt', 'r') as f:
  row = 1
  while(True):
    charList = list(f.readline().rstrip('\r\n'))
    col = 0
    for c in charList:
      col += 1
      if c == '#' or c == ' ': continue

      nodeName = 'c' + str(col) + 'r' + str(row)
      newNode = MazeNode(col, row, nodeName)
      adjListDict[nodeName] = newNode
      if c == '.': continue

      if c == 'B':
        begin = nodeName
      elif c == 'E':
        end = nodeName
      elif c in portalsDict: 
        portalsDict[c].append(nodeName)
      else:
        portalsDict[c] = [nodeName]

    if not len(charList): break
    row += 1

for key in adjListDict: 
  [name, x, y] = adjListDict[key].getInfo()
  for dir in DIRECTIONS_DICT:
    [dx, dy] = DIRECTIONS_DICT[dir]
    exitNameInDir = 'c' + str(x + dx) + 'r' + str(y + dy)
    if exitNameInDir in adjListDict:
      adjListDict[key].addExit(exitNameInDir)

for c in portalsDict: 
  (pos1, pos2) = portalsDict[c]
  adjListDict[pos1].addExit(pos2)
  adjListDict[pos2].addExit(pos1)



setDistanceFromStart(adjListDict, begin)

# for n in adjListDict: adjListDict[n].print()
# print('begin:', begin, 'end:', end)

print('# solution:', adjListDict[end].getDistance())
print('# compute time:', str(datetime.now() - startTime)[:-3])
# solution: 620
# compute time: 0:00:00.152
