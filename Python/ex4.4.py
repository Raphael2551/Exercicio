# recebe um numero e calcula o logaritmo natural

import math

numero = float(input("Digite um número para calcular o logaritmo natural: "))

if numero <= 0:
    print("O logaritmo natural não está definido para números não positivos.")
else:
    logaritmo = math.log(numero)
    print(f"O logaritmo natural de {numero} é {logaritmo:.4f}")
