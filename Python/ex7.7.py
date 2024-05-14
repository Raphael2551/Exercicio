# Faça um programa que crie um  diretório chamado "temp" e, dentro desse diretorio crie um arquivo chamado "temp.txt"

import os

def criar_diretorio_e_arquivo():
    nome_diretorio = "temp"
    nome_arquivo = "temp.txt"

    try:
        if not os.path.exists(nome_diretorio):
            os.makedirs(nome_diretorio)
            print(f"Diretório '{nome_diretorio}' criado com sucesso.")

        caminho_arquivo = os.path.join(nome_diretorio, nome_arquivo)
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write("Este é um arquivo de exemplo.")

        print(f"Arquivo '{nome_arquivo}' criado dentro do diretório '{nome_diretorio}'.")

    except Exception as e:
        print("Ocorreu um erro:", e)

criar_diretorio_e_arquivo()
