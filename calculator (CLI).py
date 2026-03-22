import math as m
import numpy as np
i = int(input("First Number:"))
i2 = int(input("Second Number(will be ignored for xʸ().):"))
o = input("Operation ('2' for x², 'rt' for √x, and '3r' for ∛x):")
if o == "+":
    print(f"Sum: {i + i2}")
elif o == "-":
    print(f"Difference: {i - i2}")
elif o == "x":
    print(f"Product: {i * i2}")
elif o == "/":
    print(f"Quotient: {str(i / i2)[:1]}\nRemainder: {i % i2}\nDecimal: {i / i2}")
elif o == "2":
    print(i ** 2)  # i² (not (√-1)² )
elif o == "rt":
    print(m.sqrt(i))
elif o == "3r":
    print(np.cbrt(i))