import math
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
WIDTH = 25
HEIGHT = 6
with open('./inputs/day8.txt', 'r') as f:
  colorBits = [int(x) for x in list(f.readline())]

layers = layeredColorBits(colorBits, WIDTH, HEIGHT)

image = [-1 for i in range(WIDTH * HEIGHT)]
for layer in layers:
  for i in range(len(layer)):
    if image[i] == -1:
      if layer[i] == 0: image[i] = ' '
      if layer[i] == 1: image[i] = 'X'

printStr = ''
for i in range(HEIGHT):
  start = i * WIDTH
  stop = (i + 1) * WIDTH
  printStr += ''.join(image[start:stop]) + '\n'

print(f'# solution: \n{printStr}\n')
print(f'# compute time: {str(datetime.now() - startTime)[:-3]}')
# solution: 2480
# compute time: 0:00:00.017
