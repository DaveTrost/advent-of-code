from datetime import datetime

def depthFirst(tree, current, depth):
  if(tree[current]['depth'] != -1): return

  tree[current]['depth'] = depth
  for child in tree[current]['children']:
    depthFirst(tree, child, depth + 1)

#
# main
#
startTime = datetime.now()
orbitsAdjacencyList = {}

# provided inputs
with open('./inputs/day6.txt', 'r') as f:
  for line in f.read().splitlines():
    (parent, child) = line.split(')')
    if not parent in orbitsAdjacencyList: 
      orbitsAdjacencyList[parent] = { 'children': [child], 'depth': -1 }
    else:
      orbitsAdjacencyList[parent]['children'].append(child)
    if not child in orbitsAdjacencyList: 
      orbitsAdjacencyList[child] = { 'children': [], 'depth': -1 }

depthFirst(orbitsAdjacencyList, 'COM', 0)

totalOrbits = 0
for key in orbitsAdjacencyList: totalOrbits += orbitsAdjacencyList[key]['depth']

print('solution:', totalOrbits)
print('compute time:', str(datetime.now() - startTime)[:-3])
# solution: 147223
# compute time: 0:00:00.006
