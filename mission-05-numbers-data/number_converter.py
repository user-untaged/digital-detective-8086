
n=int(input("Enter a decimal number: "))
if n<0:
    print("Please enter zero or a positive number.")
else:
    print("Decimal:", n)
    print("Binary:", bin(n)[2:])
    print("Hexadecimal:", hex(n)[2:].upper())
