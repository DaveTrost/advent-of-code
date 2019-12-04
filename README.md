# A repository for code challenges from the [Advent Of Code](https://adventofcode.com/2019)

## Day 1
- Part 1
  - Calculate the fuel requirements for all modules. Each module has a fuel requirement of its mass divided by three, rounded down, and subtract 2.
  - module masses provided in day1.txt
- Part 2
  - Each fuel requirement adds its own mass to the equation. Use recursion to calculate the fuel requirement of each fuel requirement, stopping when a zero or negative fuel requirement is encountered.

## Day 2
- Part 1
  - Read an Intcode program where each command in the program is 4 integers: the opcode, location of the first operand, location of the second operand, location for the solution. Print the result of the completed program, after resetting the first 2 operands.
- Part 2
  - The completed Intcode program is **intended** to report the value 19690720, and the first 2 operands must be adjusted to acheive this result. Loop through the values 0-99 for each operand, running the modified Intcode program to completetion each time, until the intended output can be acheived.

## Day 3
- Part 1
  - Follow the wires! 
  - The wiring directions are provided for 2 wires. Sequential N/S/E/W directions are converted to x,y pairs. 
  - Subsequently, each leg of the 2 wires is compared against every other leg, looking for intersection points. 
  - The intersection point closest to the 0,0 in the x/y system is chosen as the solution point
- Part 2
  - When calculating intersection points, additionally calculate the distance the 2 wires have travelled to reach the intersection
  - The intersection point with the lowest distance of travel (for both wires) is chosen as the solution point

## Day 4
- Part 1
  - Password code-breaking
  - The objective is to find the number of passwords within a numeric range comprised of 6-digit sequences. The passwords must meet the following criteria:
    * every digit in the sequence is greater than or equal to the preceeding digit
    * two digits in the sequence repeat
  - The implementation here is a straightforward loop. Time complexity is O(n)
- Part 2
  - The criteria are changed slightly:
    * every digit in the sequence is greater than or equal to the preceeding digit
    * there must be at least one group of **exactly** two repeating digits
  - implementation remains a straightforward loop. Time complexity remains at O(n)
