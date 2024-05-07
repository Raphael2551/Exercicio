# reccebe um lista de numero e utiliza um filter para retornar nova lista apenas com pares

def e_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(e_par, numeros))

print("Lista de números pares:", numeros_pares)
