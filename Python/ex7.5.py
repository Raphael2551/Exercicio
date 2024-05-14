# Crie um arquiivo vazio qualquer, com o nome digitado pelo usuário


def criar_arquivo_vazio(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
    except Exception as e:
        print("Ocorreu um erro:", e)

nome_do_arquivo = input("Digite o nome do arquivo que deseja criar: ")
criar_arquivo_vazio(nome_do_arquivo)
