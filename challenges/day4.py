from datetime import datetime
startTime = datetime.now()

def testSequentialNess(n):
  for i in range(1, 6):
    prev = int(str(n)[i - 1])
    current = int(str(n)[i])
    if prev > current: return False
  return True

def testRepeating(n):
  for i in range(1, 6):
    prev = int(str(n)[i - 1])
    current = int(str(n)[i])
    if current == prev:
      if i >= 2 and int(str(n)[i - 2]) == prev: continue
      if i <= 4 and int(str(n)[i + 1]) == current: continue
      return True
  return False

#
# main
#

# provided inputs
start = 387638
end = 919123

potentials = []
for n in range(start, end + 1):
  if not testSequentialNess(n): continue
  if not testRepeating(n): continue
  potentials.append(n)

print('solution:', len(potentials))
print('compute time:', str(datetime.now() - startTime)[:-3])
