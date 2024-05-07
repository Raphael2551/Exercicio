# crie um programa que leia varios numeros positivos digitados pelo usuario, at=é que ele digitw um valor negativo. ao fim, o programa deve mostrar a media dos numeros positivos digitados

soma = 0
contador = 0

while True:
    numero = float(input("Digite um número positivo (ou negativo para sair): "))
    
    if numero >= 0:
        soma += numero
        contador += 1
    else:
        break

if contador > 0:
    media = soma / contador
    print(f"A média dos números positivos digitados é: {media:.2f}")
else:
    print("Nenhum número positivo foi digitado.")
