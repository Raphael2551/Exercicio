# crie um generator que produza uma sequencia infinita de numeros inteiros, começando por 1. Em seguida, faça um laço para imprimir os 10 orimeiros numeros da sequencia

def gerador_infinito():
    num = 1
    while True:
        yield num
        num += 1

gerador = gerador_infinito()

for _ in range(10):
    print(next(gerador))
