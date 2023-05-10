"""
generati numere de la a la b cu pasul c
"""
def generator_nr(num1, num2, pas):
    print(f"Intervalul este: [{num1}, {num2}] cu pasul {pas}")
    for i in range(num1, num2 + 1, pas):
        yield i

nr_generate = generator_nr(3, 19, 4)
for x in nr_generate:
    print(x, end=' ')