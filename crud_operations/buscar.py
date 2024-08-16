import os 
from database.data_handler import ler_cadastro

def buscar():
    os.system('cls')
    dados = ler_cadastro()
    print("\n\033[93mBuscando um cliente\033[0m")
    nome = input("\nDigite o nome do cliente que deseja buscar: ")
    encontrado = False
    for pessoa in dados:
        if pessoa["NOME"].lower() == nome.lower():
            print("\n\033[93mCliente encontrado:\033[0m\n")
            print("\033[96m===== ",pessoa["NOME"]," =====\033[0m")
            print(f"NOME: {pessoa['NOME']}")
            print(f"EMAIL: {pessoa['EMAIL']}")
            print(f"CPF: {pessoa['CPF']}")
            print(f"TELEFONE: {pessoa['TELEFONE']}\n")
            encontrado = True
    if not encontrado:
        print("\n\033[91mCliente não encontrado!\033[0m\n")
    input("Pressione Enter para voltar...")
    os.system('cls')
