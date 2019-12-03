import math as math
with open('./inputs/day2.txt', 'r') as f:
  inputs = f.readline().split(',')

for i in range(len(inputs)): 
  inputs[i] = int(inputs[i])

for noun in range(99):
  for verb in range(99):
    tempList = inputs[0:len(inputs)]
    tempList[1] = noun
    tempList[2] = verb

    for i in range(0, len(tempList), 4): 
      op, pos1, pos2, posResult = tempList[i:i+4]
      if op == 99: break
      if op == 1: 
        tempList[posResult] = tempList[pos1] + tempList[pos2]
      if op == 2: 
        tempList[posResult] = tempList[pos1] * tempList[pos2]
    
    if tempList[0] == 19690720:
      print(noun, verb)
      break
