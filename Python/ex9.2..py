# Crie um programa que recebe uma lista de numeros e retorne a media aritmética deles. Trate exxceções caso a lista seja vazia ou contenha valores não numericos

def calcular_media(lista_numeros):
    try:
        if not lista_numeros:
            raise ValueError("A lista está vazia. Não é possível calcular a média.")
        
        numeros_validos = [float(num) for num in lista_numeros if num.isdigit() or (num[0] == '-' and num[1:].isdigit())]
        
        if not numeros_validos:
            raise ValueError("A lista não contém valores numéricos válidos.")
        
        media = sum(numeros_validos) / len(numeros_validos)
        return media
    
    except ValueError as e:
        print(e)
        return None
    except Exception as e:
        print("Ocorreu um erro:", e)
        return None


numeros = input("Digite os números separados por espaço: ").split()

media = calcular_media(numeros)
if media is not None:
    print(f"A média dos números é: {media:.2f}")
