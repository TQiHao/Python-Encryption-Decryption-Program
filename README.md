# Python Encryption & Decryption Program

A Python program that implements a simple encryption and decryption algorithm for 4-digit integers.

## Program Description
This program provides both encryption and decryption functionality:
- **Encryption**: Transforms 4-digit numbers using digit manipulation and swapping
- **Decryption**: Reverses the encryption process to recover original numbers

## Encryption Algorithm
1. Take a 4-digit integer (abcd)
2. Add 7 to each digit and apply modulus 10
3. Swap positions: 1st↔3rd digit, 2nd↔4th digit
4. Output encrypted result

## Decryption Algorithm  
1. Take encrypted 4-digit integer
2. Add 3 to each digit and apply modulus 10
3. Swap positions: 1st↔3rd digit, 2nd↔4th digit
4. Output original number

## Features
- Interactive command-line interface
- Input validation for 4-digit integers
- Mathematical encryption/decryption
- Clear step-by-step digit manipulation

## How to Run
```bash
python encryption_program.py

Enter a 4 digits integer for encryption: 1234
==> Encrypted integer is 0189

Enter a 4 digits integer for decryption: 0189  
==> Decrypted integer is 1234

## Files
- `encryption_program.py` - Complete encryption/decryption implementation

## Technologies Used
- Python 3
- Mathematical operations
- String manipulation
- Algorithm design

## Author
Toh Qi Hao
