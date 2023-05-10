"""
generati primele numere pana la a divizibile cu b
"""
def generator_divisors(a, b):
    for i in range(0, a + 1, b):
        yield i

generated_divisors = generator_divisors(23, 4)
for x in generated_divisors:
    print(x, end=' ')