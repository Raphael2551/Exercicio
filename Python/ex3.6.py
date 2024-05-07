# crie um programa que some e mostre os numeros impares de  1 a 100

soma = 0

for numero in range(1, 101):
     if numero % 2 != 0:
        soma += numero
        print(numero)

print("A soma dos números de 1 a 100 é:", soma)
