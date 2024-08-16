import os 
from database.data_handler import ler_cadastro, escrever_cadastro


def excluir():
    os.system('cls')
    dados = ler_cadastro()
    print("\n\033[93mExcluindo um cliente\033[0m")
    nome = input("\nDigite o nome do cliente que deseja excluir: ")   
    encontrado = False
    for pessoa in dados:
        if pessoa['NOME'].lower().strip() == nome.lower().strip():
            encontrado = True
            dados.remove(pessoa)
            escrever_cadastro(dados)
            print("\n\033[92mCliente excluído com sucesso!\033[0m\n")
            break
    if not encontrado:
        print("\n\033[91mCliente não encontrado.\n\033[0m")
    input("Pressione Enter para voltar...")
    os.system('cls')