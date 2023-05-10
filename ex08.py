"""
generati numerele de la x la 1, din y in y (sare peste y numere, ca in primul
exercitiu)
"""
def reversed_num_gen(num, step):
    for i in range(num, 0, -1*step):
        yield i

generated_nums_in_reverse= reversed_num_gen(19, 4)
for x in generated_nums_in_reverse:
    print(x, end=' ')