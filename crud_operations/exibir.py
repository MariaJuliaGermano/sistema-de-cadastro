import os
from storage.data_handler import ler_cadastro

def exibir():
    os.system("cls")
    dados = ler_cadastro()
    if dados:
        print("\n\033[93mExibindo clientes cadastrados:\033[0m\n")
        for pessoa in dados:
            print("\033[96m===== ",pessoa["NOME"]," =====\033[0m")
            print(f"NOME: {pessoa['NOME']}")
            print(f"EMAIL: {pessoa['EMAIL']}")
            print(f"CPF: {pessoa['CPF']}")
            print(f"TELEFONE: {pessoa['TELEFONE']}\n")
    else:
        print("\n\033[91mNão há pessoas cadastradas.\033[0m\n")
    input("Pressione Enter para voltar...")
    os.system('cls')