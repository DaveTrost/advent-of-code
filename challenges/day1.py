import math as math
with open('./inputs/day1.txt', 'r') as f:
  moduleMasses = f.read().splitlines()

def fuelCalculation(mass):
  fuel = math.floor(int(mass) / 3) - 2
  if fuel <= 0: return 0
  return fuel + fuelCalculation(fuel)

sum = 0
for m in moduleMasses: 
  sum += fuelCalculation(m)
print(sum)
