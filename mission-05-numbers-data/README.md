# Mission 5 - Numbers and Data

## 1. Task / objective
Convert decimal, binary and hexadecimal values, verify results with python, build a small converter and explain text encoding.

## 2. Work completed

### Task 5.1 - Convert numbers by hand 

| Question | Working | Answer |
|---|---|---|
| Convert decimal 13 to binary | 13 = 8 + 4 + 1 | 1101 |
| Convert decimal 25 to binary | 25 = 16 + 8 + 1 | 11001 |
| Convert binary 1010 to decimal | 1×8 + 0×4 + 1×2 + 0×1 | 10 |
| Convert binary 1101 to decimal | 1×8 + 1×4 + 0×2 + 1×1 | 13 |
| Convert hexadecimal A to decimal | A represents 10 | 10 |
| Convert hexadecimal 1F to decimal | 1×16 + 15 (F represents 15)  | 31 |
| Convert binary 1111 to hexadecimal | 1111 is 15 (8+4+2+1) in decimal and 15 == F in hexadecimal | F |

### Task 5.2 - Verify using python

| Expression | Result | Match? |
|---|---|---|
| bin(13) | '0b1101' | Yes |
| bin(25) | '0b11001' | Yes |
| int('1010', 2) | 10 | Yes |
| int('1101', 2) | 13 | Yes |
| hex(10) | '0xa'| Yes |
| int('1F', 16) | 31 | Yes |
| hex(int('1111', 2))[2:].upper() | 'F' | Yes |
