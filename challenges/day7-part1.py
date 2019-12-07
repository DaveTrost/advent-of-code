from datetime import datetime
import itertools


def intCodeComputer(in1, in2):
  with open('./inputs/day7.txt', 'r') as f:
    intCode = [int(x) for x in f.readline().split(',')]

  input = in1
  opIndex = 0
  code = 0
  while True:
    opWith5Chars = f'{intCode[opIndex]:05d}'
    (_, modeParam2, modeParam1, opTensDigit, opOnesDigit) = [int(x) for x in list(opWith5Chars)]
    op = opTensDigit * 10 + opOnesDigit

    if op == 99: 
      return code

    if op == 1 or op == 2 or op == 7 or op == 8: 
      param1 = intCode[opIndex + 1] if modeParam1 == 1 else intCode[intCode[opIndex + 1]]
      param2 = intCode[opIndex + 2] if modeParam2 == 1 else intCode[intCode[opIndex + 2]]
      resultPosition = intCode[opIndex + 3]
      if op == 1: result = param1 + param2
      if op == 2: result = param1 * param2
      if op == 7: result = 1 if param1 < param2 else 0
      if op == 8: result = 1 if param1 == param2 else 0
      intCode[resultPosition] = result
      opIndex += 4

    if op == 3 or op == 4:
      if op == 3:
        savePosition = intCode[opIndex + 1]
        intCode[savePosition] = input
        input = in2
      if op == 4 and modeParam1 == 1:
        code = intCode[opIndex + 1]
      if op == 4 and modeParam1 == 0:
        address = intCode[opIndex + 1]
        code = intCode[address]
      opIndex += 2

    if op == 5 or op == 6:
      param1 = intCode[opIndex + 1] if modeParam1 == 1 else intCode[intCode[opIndex + 1]]
      param2 = intCode[opIndex + 2] if modeParam2 == 1 else intCode[intCode[opIndex + 2]]
      newIndex = opIndex + 3
      if op == 5 and param1 != 0: newIndex = param2  # jump if true
      if op == 6 and param1 == 0: newIndex = param2  # jump if false
      opIndex = newIndex

#
# main
#
startTime = datetime.now()

max = 0
combos = itertools.permutations('01234', 5)
for c in combos:
  input = 0
  phaseCodes = [int(x) for x in c]
  for code in phaseCodes:
    input = intCodeComputer(code, input)
  if input > max:
    max = input
    maxSettings = phaseCodes

print('# solution:', max, '(from settings:', maxSettings, ')')
print('# compute time:', str(datetime.now() - startTime)[:-3])
# solution: 340
# compute time: 0:00:00.012
