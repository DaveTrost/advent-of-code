from datetime import datetime
startTime = datetime.now()

# provided inputs
start = 387638
end = 919123

potentials = []
for n in range(start, end + 1):
  valid = True
  repeating = False
  for i in range(1, 6):
    current = int(str(n)[i - 1])
    next = int(str(n)[i])
    if next == current: repeating = True
    if next < current: 
      valid = False
      break
  if valid and repeating: potentials.append(n)

print('solution:', len(potentials))
print('compute time:', str(datetime.now() - startTime)[:-3])
