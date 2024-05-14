# faça um programa que criei um diretorio chamado "Textos" e que, dentro dessediretorio crie3 aruivos "arquivo1.txt","arquivo2.txt" e "arquivo3.txt" todos contendo o texto "Python Essencial". Em seguida, o prograa deve criar um arquivo compactado (.zip) contendo o diretorio "Textos"

import os
import zipfile

def criar_arquivos_texto_e_zip():
    nome_diretorio = "Textos"
    nomes_arquivos = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt"]
    conteudo_arquivo = "Python Essencial"

    try:
        if not os.path.exists(nome_diretorio):
            os.makedirs(nome_diretorio)
            print(f"Diretório '{nome_diretorio}' criado com sucesso.")

        for nome_arquivo in nomes_arquivos:
            caminho_arquivo = os.path.join(nome_diretorio, nome_arquivo)
            with open(caminho_arquivo, 'w') as arquivo:
                arquivo.write(conteudo_arquivo)
            print(f"Arquivo '{nome_arquivo}' criado dentro do diretório '{nome_diretorio}'.")

        with zipfile.ZipFile('Textos.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
            for pasta_raiz, pastas, arquivos in os.walk(nome_diretorio):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(pasta_raiz, arquivo)
                    caminho_no_zip = os.path.relpath(caminho_completo, nome_diretorio)
                    zipf.write(caminho_completo, arcname=caminho_no_zip)
            print("Arquivo compactado 'Textos.zip' criado com sucesso.")

    except Exception as e:
        print("Ocorreu um erro:", e)

criar_arquivos_texto_e_zip()
