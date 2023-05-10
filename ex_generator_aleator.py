import random
import copy

def unique_random_generator(lista_de_studenti):
    lista_ramasi = copy.deepcopy(lista_de_studenti)
    while len(lista_ramasi) > 0:
        student_chemat = random.choice(lista_ramasi)
        lista_ramasi.remove(student_chemat)
        yield  student_chemat

lista_studenti = ["Nicolae Tancau", "Vlad Duma", "Alina Capota", "Sanda Rus", "Mario Musat", "Daniel Ojog", "Alex Tofan", "Bogdan Chisu"]

for st in unique_random_generator(lista_studenti):
    print(st)
