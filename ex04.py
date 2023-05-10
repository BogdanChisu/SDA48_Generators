"""
generati patratul numarului daca este par, si cubul sau daca e impar, pentru
un interval de la a la b
"""
from math import sqrt

def generator_cubes(num1, num2):
    print(f"Intervalul este: [{num1}, {num2}]")
    for i in range(num1, num2 + 1):
        if i % 2 == 1:
            yield i ** 3
        else:
            yield i ** 2

cubes_generate = generator_cubes(3, 7)
for x in cubes_generate:
    print(x, end=' ')