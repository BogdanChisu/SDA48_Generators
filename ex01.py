"""
2 functii ce returneaza patratul nr-lor de la 1 la x

1 prin metoda generatoarelor
2 prin returnarea unei liste cu toate numerele deodata
"""
from time import perf_counter
def patrate_generator(nr):
    for i in range (1, nr+1):
        yield i * i

def patrate_clasic(nr):
    lista_patrate = []
    for i in range(1, nr + 1):
        lista_patrate.append(i * i)
    return lista_patrate


# performanta unui generator este semnificativ mai mare decat prin a genera toate rezultatele deodata
start_gen = perf_counter()
patrat_gen = patrate_generator(100000)
print(patrat_gen)
print(f"pentru gen = {perf_counter() - start_gen}")
start_cla = perf_counter()
patrate_clasic = patrate_clasic(100000)
# print(patrate_clasic)
print(f"pentru cla = {perf_counter() - start_cla}")