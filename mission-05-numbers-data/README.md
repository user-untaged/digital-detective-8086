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

### Task 5.3 - Build a small number converter


### Task 5.4 - How is text stored?
### Number converter
I ran `number_converter.py` with three positive values.

| Input | Binary output | Hexadecimal output |
|---:|---:|---:|
| 13 | `1101` | `D` |
| 25 | `11001` | `19` |
| 42 | `101010` | `2A` |

The program uses `input()` to read what I type and `int()` to turn it into a whole number. `bin()` converts it to binary, and `hex()` converts it to hexadecimal. The program removes the `0b` or `0x` prefix from the display; it also makes the hexadecimal letters uppercase.

### Text encoding
- Uppercase `A` has ASCII decimal code `65`.
- Lowercase `a` has ASCII decimal code `97`.
- A computer needs an encoding standard to store characters as numbers and read them consistently. The rupee sign (`₹`) is an example of a character that is not part of basic ASCII; UTF-8 can represent it.


## 3. Commands / tools used
- `python3`: opened for the conversion checks
- `python3 number_converter.py`: ran the converter from this file

## 4. My understanding
How to convert between different forms of numbers (decimal, binary, hexadecimal). Python's conversion functions helped me check the answers, and the converter uses those functions to display the binary and hexadecimal forms of a decimal number.

## 5. Difficulties faced
I found it difficult to verify the conversions using python.

## 6. How I resolved them
With the help of my friend and AI, I learnt and verified.

## 7. Evidence / files
- [`number_converter.py`](mission-05-numbers-data/number_converter.py): the working converter

## 8. Commit details
Commit message: `Build number converter and practice data representation`
Status: Committed and pushed.
