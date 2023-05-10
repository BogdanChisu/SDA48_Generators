# lista_x = [1, 2, 3]
# for x in lista_x:
#     print(x)
#
# strx = 'abc'
# for x in strx:
#     print(x)
#
# tuplex = (4, 5, 6)
# for x in tuplex:
#     print(x)
#
# lista_x[0] = 8
# print(lista_x)
# tuplex[0] = 9
# # asignarea va da eroare pentru ca tuple e immutable spre deosebire de liste

# set este o lectie de elemente neordonate si unice
# setx = {11, 12, 13}
# for x in setx:
#     print(x)
# import math
#
# def is_prime(numberx):
#     for i in range(2, int(math.sqrt(numberx)+ 1)):
#         if numberx % i == 0:
#             return False
#     return True
#
# def prime_generator(numar):
#     num_start = 2
#     generated_numbers = 0
#     while generated_numbers <= numar:
#         if is_prime(num):
#             yield num
#             generated_numbers += 1
#         num += 1
#
# prime_generator(1000)
path_to_file = "file1.txt"
def read_file_via_generator(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

def read_file_classical_approach(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
    return text

file_text_clasic = read_file_classical_approach(path_to_file)
print(file_text_clasic)

file_gen = read_file_via_generator(path_to_file)
print(file_gen)
for rand in file_gen:
    print(rand)