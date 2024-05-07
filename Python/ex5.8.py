# crie uma funcao chamada decodifiar que recebe um texo e aplica a seguinte regra: toda letra deve ser rescrita para a letra anterior no alfabeto. utilizar de fomr arecursiva
def decodificar(texto):
    if len(texto) == 0:
        return texto
    
    codigo = ord(texto[-1])
    
    if codigo >= 65 and codigo <= 90:
        codigo -= 1
        if codigo < 65:
            codigo = 90
    elif codigo >= 97 and codigo <= 122:
        codigo -= 1
        if codigo < 97:
            codigo = 122
    else:
        codigo = ord(texto[-1])
    
    return decodificar(texto[:-1]) + chr(codigo)

# Teste da função
texto_codificado = "bcdefghijklmnopqrstuvwxyza"
texto_decodificado = decodificar(texto_codificado)
print("Texto decodificado:", texto_decodificado)
