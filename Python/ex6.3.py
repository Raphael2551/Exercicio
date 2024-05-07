# use list comprehension para cirar lista quadrada dos pares de 1 a 100

lista_quadrados_pares = [x**2 for x in range(1, 11) if x % 2 == 0]

print("Lista dos quadrados dos números pares de 1 a 100:", lista_quadrados_pares)
