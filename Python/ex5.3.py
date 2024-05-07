# funcao com 3 parametros: 1 INT, 1 REAL e 1 texto, imprimir os valores dos parametros

def imprimir_valores(numero_inteiro, numero_real, texto):
    print(f"Valor do número inteiro: {numero_inteiro}")
    print(f"Valor do número real: {numero_real}")
    print(f"Texto inserido: {texto}")

numero_int = 10
numero_real = 3.14
texto = "Olá, mundo!"

imprimir_valores(numero_int, numero_real, texto)
