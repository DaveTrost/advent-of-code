from datetime import datetime

#
# main
#
startTime = datetime.now()

# provided inputs
with open('./inputs/day5.txt', 'r') as f:
  intCode = [int(x) for x in f.readline().split(',')]

opIndex = 0
code = 0
while True:
  opWith5Chars = f'{intCode[opIndex]:05d}'
  (modeResult, modeParam2, modeParam1, opTensDigit, opOnesDigit) = [int(x) for x in list(opWith5Chars)]
  op = opTensDigit * 10 + opOnesDigit

  if op == 99: break

  if op == 1 or op == 2: 
    param1 = intCode[opIndex + 1] if modeParam1 == 1 else intCode[intCode[opIndex + 1]]
    param2 = intCode[opIndex + 2] if modeParam2 == 1 else intCode[intCode[opIndex + 2]]
    resultPosition = intCode[opIndex + 3]
    if op == 1: result = param1 + param2
    if op == 2: result = param1 * param2
    intCode[resultPosition] = result
    print(f'op_{opWith5Chars} ... param 1 = {intCode[opIndex + 1]}->{param1} param 2 = {intCode[opIndex + 2]}->{param2}')
    print(f'stored {result} to address {resultPosition}')
    opIndex += 4

  if op == 3 or op == 4:
    if op == 3:
      savePosition = intCode[opIndex + 1]
      intCode[savePosition] = 1
      print('op =', opWith5Chars)
      print(f'stored `1` to address {savePosition}')
    if op == 4 and modeParam1 == 1:
      code = intCode[opIndex + 1]
      print('op =', opWith5Chars)
      print(f'diagnostic code from parameter = {code}')
    if op == 4 and modeParam1 == 0:
      address = intCode[opIndex + 1]
      code = intCode[address]
      print('op =', opWith5Chars)
      print(f'diagnostic code from address ({address}) = {code}')
    opIndex += 2

print('solution:', code)
print('compute time:', str(datetime.now() - startTime)[:-3])
# solution: 9431221
# compute time: 0:00:00.022


