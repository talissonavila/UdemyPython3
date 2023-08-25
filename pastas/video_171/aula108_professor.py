# Solução 1
lista_a = [10, 2, 3, 44, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = []
for count in range(len(lista_b)):
    lista_soma.append(lista_a[count] + lista_b[count])

print(f'Solução 1: {lista_soma}')


# Solução 2
lista_a = [10, 2, 3, 44, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = []
for count, _ in enumerate(lista_b):
    lista_soma.append(lista_a[count] + lista_b[count])

print(f'Solução 2: {lista_soma}')


# Solução 3
lista_a = [10, 2, 3, 44, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = [x + y for x,y in zip(lista_a, lista_b)]

print(f'Solução 3: {lista_soma}')
