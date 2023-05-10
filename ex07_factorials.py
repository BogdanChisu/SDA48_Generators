"""
generati factorialele pana la x
"""

def factorials_generator(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
        yield factorial

generated_factorials = factorials_generator(5)
for x in generated_factorials:
    print(x, end=' ')