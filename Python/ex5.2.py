# crie uma funcao que recebe 1 int, retorna true para par e false para impar. depois chama a funcao passando valores

def par_ou_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero1 = 5
resultado1 = par_ou_impar(numero1)
print(f"O número {numero1} é par? {resultado1}")

numero2 = 8
resultado2 = par_ou_impar(numero2)
print(f"O número {numero2} é par? {resultado2}")
