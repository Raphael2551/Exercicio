# implemente um jogo de adivinhação em que o ususário deve acertar uma palavra secreta. Utilize tratamento de exceção para garantir que o user insira apenas letras do alfabeto

import string
import random

def adivinhacao(palavra_secreta):
    tentativas = 3
    letras_corretas = set()
    
    while tentativas > 0:
        letra = input("\nDigite uma letra: ").lower()
        
        if len(letra) != 1 or letra not in string.ascii_lowercase:
            print("Erro: Digite apenas uma letra do alfabeto.")
            continue
        
        if letra in letras_corretas:
            print("Você já tentou essa letra.")
            continue
        
        if letra in palavra_secreta:
            letras_corretas.add(letra)
            print("Letra correta!")
        else:
            tentativas -= 1
            print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")
        
        palavra_descoberta = ''.join(l if l in letras_corretas else '_' for l in palavra_secreta)
        print(f"Palavra descoberta: {palavra_descoberta}")
        
        if palavra_descoberta == palavra_secreta:
            print("Parabéns! Você acertou a palavra secreta.")
            return
        
    print(f"Game over! A palavra secreta era '{palavra_secreta}'.")

palavras_secretas = ["python", "programacao", "desafio", "jogo"]

palavra_secreta = random.choice(palavras_secretas)

print("Bem-vindo ao jogo de adivinhação!")
print("A palavra secreta tem", len(palavra_secreta), "letras.")
adivinhacao(palavra_secreta)
