# leia um txt e exibi o numero de linhas

def contar_linhas_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            num_linhas = len(linhas)
            print(f"O arquivo '{nome_arquivo}' possui {num_linhas} linhas.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print("Ocorreu um erro:", e)


nome_do_arquivo = input("Digite o nome e caminho do arquivo: ")
contar_linhas_arquivo(nome_do_arquivo)
