# crie um programa que verifca se o texto digitado pelo usuário é um palindromo ou noa (use texto[::-1]para obter o texto invertido)

texto = input("Digite um texto: ")

texto_sem_espacos = texto.replace(" ", "").lower()

texto_invertido = texto_sem_espacos[::-1]

if texto_sem_espacos == texto_invertido:
    print("O texto digitado é um palíndromo.")
else:
    print("O texto digitado não é um palíndromo.")
