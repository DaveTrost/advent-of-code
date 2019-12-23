from datetime import datetime

def addEleToList(l, ele, neighbor):
  if not ele in l: 
    l[ele] = { 'neighbors': [neighbor], 'depth': -1}
  else:
    l[ele]['neighbors'].append(neighbor)

def createAdjacencyList(filename):
  adjList = {}
  with open(filename, 'r') as f:
    for line in f.read().splitlines():
      (orbited, orbiter) = line.split(')')
      addEleToList(adjList, orbited, orbiter)
      addEleToList(adjList, orbiter, orbited)
  return adjList

def markDepths(graph, current, depth):
  if(graph[current]['depth'] != -1): return

  graph[current]['depth'] = depth
  for neighbor in graph[current]['neighbors']:
    if(graph[neighbor]['depth'] == -1):
      markDepths(graph, neighbor, depth + 1)

#
# main
#
startTime = datetime.now()

orbitsAdjacencyList = createAdjacencyList('./inputs/day6.txt')
markDepths(orbitsAdjacencyList, 'SAN', 0)

print('# solution:', orbitsAdjacencyList['YOU']['depth'] - 2)
print('# compute time:', str(datetime.now() - startTime)[:-3])
# solution: 340
# compute time: 0:00:00.012
