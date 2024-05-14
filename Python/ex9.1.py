# Crie um programa que solicite ao usuario dois numeros inteiros e exiba a divisao do primeiro pelo segundo. trate excessoes de devisa por 0

def dividir_numeros():
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        
        if num2 == 0:
            raise ZeroDivisionError("Erro: divisão por zero não é permitida.")
        
        resultado = num1 / num2
        print(f"O resultado da divisão de {num1} por {num2} é {resultado:.2f}")
    
    except ValueError:
        print("Erro: digite apenas números inteiros.")
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print("Ocorreu um erro:", e)

dividir_numeros()
