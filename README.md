# A repository for code challenges from the [Advent Of Code](https://adventofcode.com/2019)

## Day 1
- Part 1
  - Calculate the fuel requirements for all modules. Each module has a fuel requirement of its mass divided by three, rounded down, and subtract 2.
  - module masses provided in day1.txt
- Part 2
  - Each fuel requirement adds its own mass to the equation. Use recursion to calculate the fuel requirement of each fuel requirement, stopping when a zero or negative fuel requirement is encountered.
