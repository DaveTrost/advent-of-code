# A repository for code challenges from the [Advent Of Code](https://adventofcode.com/2019)

## Day 1
- Part 1
  - Calculate the fuel requirements for all modules. Each module has a fuel requirement of its mass divided by three, rounded down, and subtract 2.
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

## Day 5
- Part 1
  - New Intcode definition:
    * 1st parameter: opcode
      * 01: add - takes 3 parameters
      * 02: multiply - takes 3 parameters
      * 03: save to location - takes 1 parameter
      * 04: read from location (aka: output) - takes 1 parameter
    * 2nd parameter: a location or a value
    * 3rd parameter (optional): a location or a value
    * 4th parameter (optional): location for the solution
  - NOTE: because some instructions need only 1 parameter, instruction size is no longer constant.
  - The opcode itself is extended to be up to 5 digits, described as ABCDE, where: 
    * A - mode of 3rd parameter: 1 = use as value, 0 = use as location (should always be zero, I think?)
    * B - mode of 2nd parameter: 1 = use as value, 0 = use as location
    * C - mode of 1st parameter: 1 = use as value, 0 = use as location
    * DE - two-digit opcode
  - The provided input is a program that uses the new instruction set and outputs diagnostic codes (using the output opcode). If the Intcode computer is programmed properly, each diagnostic output should report zero. Except for the final diagnostic output - this diagnostic output is the expected answer - ostensibly needed to repair the space shuttle's air conditioning system(?)
  - The instructions say to provide `1` as the value to the first input-type opcode
- Part 2
  - New Intcode op definitions:
      * 05: jump-if-true - takes 2 parameters. If parameter 1 is non-zero, set the instruction pointer to parameter 2's value
      * 06: jump-if-false - takes 2 parameters. If parameter 1 is zero, set the instruction pointer to parameter 2's value
      * 07: less than - takes 3 parameters. If parameter 1 < parameter 2, store `1` in the position of parameter 3, else store `0` there
      * 08: equal to - takes 3 parameters. If parameter 1 == parameter 2, store `1` in the position of parameter 3, else store `0` there
  - The provided input will no longer output diagnostic codes. Instead, the single output will be the expected answer - ostensibly needed to repair the thermal radiators of the space shuttle's air conditioning system(?)
  - The instructions say to provide `5` as the value to the first input-type opcode
