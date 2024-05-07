# crie um programa que verifca se o texto digitado pelo usuário é um número interito ou nao e mostre uma mensagem de acordo (use texto.isdigit() para verficar)

texto = input("Digite um texto: ")

if texto.isdigit():
    print("O texto digitado é um número inteiro.")
else:
    print("O texto digitado não é um número inteiro.")
