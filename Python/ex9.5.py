# crie uma funcao que leia um arquivo de texto e exiba o conteudo na tela. Trate exceções caso o arquivo não exista ou não seja possível vê-lo

def exibir_conteudo_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except PermissionError:
        print("Erro: Sem permissão para acessar o arquivo.")
    except Exception as e:
        print("Ocorreu um erro:", e)

nome_do_arquivo = input("Digite o nome do arquivo (inclua o caminho se estiver em outro diretório): ")
exibir_conteudo_arquivo(nome_do_arquivo)
