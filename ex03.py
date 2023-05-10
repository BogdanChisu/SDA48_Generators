"""
generati radacina patrata a numerelor din intervalul a,b. Rotunjiti acestea
la 2 decimale.
"""

from math import sqrt

def generator_sqrt(num1, num2):
    print(f"Intervalul este: [{num1}, {num2}]")
    for i in range(num1, num2 + 1):
        yield round(sqrt(i), 2)

sqrt_generate = generator_sqrt(3, 7)
for x in sqrt_generate:
    print(x, end=' ')