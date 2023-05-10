"""
generati elementele dintr-o lista care respecta o conditie (conditia definita
cu lambda)
"""

def lambda_generator(lst):
    for i in lst:
        calc = lambda i : i if i >= 5 else None
        if calc(i):
            yield calc(i)


my_list = [2, 3, 6, 7, 5]
my_lambda_lst = lambda_generator(my_list)
for x in my_lambda_lst:
    print(x, end=' ')