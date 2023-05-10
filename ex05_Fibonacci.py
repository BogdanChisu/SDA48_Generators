"""
generati primele x numere ale lu Fibonacci
"""

def fibonacci_generator(num):
    print(f"Requested {num} Fibonacci numbers")
    a = 1
    b = 1
    for i in range(1, num + 1):
        if i == 1 or i == 2:
            yield 1
        else:
            c = a + b
            yield c
            a = b
            b = c

generated_fibonaccies = fibonacci_generator(8)
for x in generated_fibonaccies:
    print(x, end = ' ')