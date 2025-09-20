import os
import loader

def imprimir_titulo():
    print("""
        ██╗░░░░░███████╗██╗████████╗░█████╗░██████╗░  ██████╗░███████╗  ███╗░░██╗░█████╗░████████╗░█████╗░
        ██║░░░░░██╔════╝██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██╔════╝  ████╗░██║██╔══██╗╚══██╔══╝██╔══██╗
        ██║░░░░░█████╗░░██║░░░██║░░░██║░░██║██████╔╝  ██║░░██║█████╗░░  ██╔██╗██║██║░░██║░░░██║░░░███████║
        ██║░░░░░██╔══╝░░██║░░░██║░░░██║░░██║██╔══██╗  ██║░░██║██╔══╝░░  ██║╚████║██║░░██║░░░██║░░░██╔══██║
        ███████╗███████╗██║░░░██║░░░╚█████╔╝██║░░██║  ██████╔╝███████╗  ██║░╚███║╚█████╔╝░░░██║░░░██║░░██║
        ╚══════╝╚══════╝╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝  ╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝

        ███████╗██╗░██████╗░█████╗░░█████╗░██╗░░░░░
        ██╔════╝██║██╔════╝██╔══██╗██╔══██╗██║░░░░░
        █████╗░░██║╚█████╗░██║░░╚═╝███████║██║░░░░░
        ██╔══╝░░██║░╚═══██╗██║░░██╗██╔══██║██║░░░░░
        ██║░░░░░██║██████╔╝╚█████╔╝██║░░██║███████╗
        ╚═╝░░░░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝""")
    print("\n1 --> ler pasta e criar planilha.")
    print("2 --> ler arquivo individual.")
    print("0 --> sair.")
    
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

opcao = None
 
while opcao != 0:
    limpar_tela()
    imprimir_titulo()
    opcao = input("digite uma opção: ")
    opcao = int(opcao)
    
    match opcao:
        case 1:
            limpar_tela()
            nome_planilha = "notas_fiscais_financiaveis.xlsx"
            caminho = input("digite o caminho da pasta em que a planilha será criada: ")
            if caminho.endswith('"'):
                caminho = caminho.strip('"')
            caminho_completo = os.path.join(caminho, nome_planilha)

            caminho_pasta = input("digite o caminho da pasta com as notas fiscais: ")
            if caminho_pasta.endswith('"'):
                caminho_pasta = caminho_pasta.strip('"')

            loader.processar_pasta(caminho_pasta, caminho_completo)
           
            opcao = int(input("\ndigite qualquero numro para voltar ao menu ou 0 para sair: "))

        case 2:
            limpar_tela()
            caminho_arquivo = input("digite o caminho do arquivo: ")
            if caminho_arquivo.endswith('"'):
                caminho_arquivo = caminho_arquivo.strip('"')
            
            loader.processar_arquivo_individual(caminho_arquivo)

            opcao = int(input("\ndigite qualquero numro para voltar ao menu ou 0 para sair: "))
        case 0:
            break
        case _:
            print("opção invalida")

