import math
import sys
from datetime import datetime

def layeredColorBits(colorBits, w, h):
  layerSize = w * h
  layers = []
  for i in range(math.floor(len(colorBits) / layerSize)):
    start = i * layerSize
    stop = (i + 1) * layerSize
    layers.append(colorBits[start:stop])
  return layers

#
# main
#
startTime = datetime.now()

# inputs
with open('./inputs/day8.txt', 'r') as f:
  colorBits = [int(x) for x in list(f.readline())]

layers = layeredColorBits(colorBits, 25, 6)

min = sys.maxsize
for layer in layers:
  countZeroes = 0
  countOnes = 0
  countTwos = 0
  for x in layer: 
    if x == 0: countZeroes += 1
    if x == 1: countOnes += 1
    if x == 2: countTwos += 1
  if countZeroes < min: 
    min = countZeroes
    product = countOnes * countTwos

print('# solution:', product)
print('# compute time:', str(datetime.now() - startTime)[:-3])
# solution: 2480
# compute time: 0:00:00.017
