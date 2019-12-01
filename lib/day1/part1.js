const fs = require('fs');
const moduleMasses = fs.readFileSync('./inputs/day1.txt').toString().split('\n');

const answer = moduleMasses.reduce((acc, n) => acc + fuelNeeded(n), 0);
console.log(answer);

function fuelNeeded(n) {
  const initialFuelCalc = Math.floor(n / 3) - 2;
  return initialFuelCalc <= 0 ? 0 : initialFuelCalc + fuelNeeded(initialFuelCalc);
}
