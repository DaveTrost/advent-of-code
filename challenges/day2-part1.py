with open('./inputs/day2.txt', 'r') as f:
  inputs = f.readline().split(',')

for i in range(len(inputs)): 
  inputs[i] = int(inputs[i])

inputs[1] = 12
inputs[2] = 2

for i in range(0, len(inputs), 4): 
  op, pos1, pos2, posResult = inputs[i:i+4]
  if op == 99: break
  if op == 1: 
    inputs[posResult] = inputs[pos1] + inputs[pos2]
  if op == 2: 
    inputs[posResult] = inputs[pos1] * inputs[pos2]

print(inputs)
