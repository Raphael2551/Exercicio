# crie uma funcao que recebe um int e imprime uma contagem regressiva

def contagem_regressiva():
    numero = int(input("Digite um número para iniciar a contagem regressiva: "))
    while numero >= 0:
        print(numero)
        numero -= 1

# Chamada da função
contagem_regressiva()
