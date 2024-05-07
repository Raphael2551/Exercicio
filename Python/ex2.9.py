# media de 3 numeros, > 6 aprovado

numero1 = int(input("Digite um numero1: "))
numero2 = int(input("Digite um numero2: "))
numero3 = int(input("Digite um numero3: "))

media = (numero1*numero2*numero3)/3

if media > 6:
    print(f"Aprovado")
else:
    print(f"Reprovado")