import os 
from database.data_handler import ler_cadastro, escrever_cadastro

def atualizar():
    os.system('cls')
    dados = ler_cadastro()
    print("\n\033[93mAtualizando um cliente\033[0m")
    nome = input("\nDigite o nome do cliente que deseja atualizar: ")
    clientes = []
    for pessoa in dados:
        if pessoa['NOME'].lower() == nome.lower():
            clientes.append(pessoa)
    
    for i, pessoa in enumerate(clientes):
        pessoa["id"] = i +1

    if clientes:
        print("\n\033[93mClientes encontrados:\033[0m")
        for pessoa in clientes:
            print("\033[96m===== ", pessoa["NOME"]," =====\033[0m")
            print(f"ID: {pessoa["id"]}")
            print(f"NOME: {pessoa['NOME']}")
            print(f"EMAIL: {pessoa['EMAIL']}")
            print(f"CPF: {pessoa['CPF']}")
            print(f"TELEFONE: {pessoa['TELEFONE']}\n")
        id = int(input("Selecione o ID do cliente que deseja atualizar: "))
        for pessoa in clientes:
            if pessoa["id"] == id:
                pessoa['NOME'] = input(f"NOME: {pessoa["NOME"]} --> NOVO NOME: ")
                pessoa['EMAIL'] = input(f"EMAIL: {pessoa["EMAIL"]} --> NOVO EMAIL: ")
                pessoa['CPF'] = int(input(f"CPF: {pessoa["CPF"]} --> NOVO CPF: "))
                pessoa['TELEFONE'] = int(input(f"TELEFONE: {pessoa["TELEFONE"]} --> NOVO TELEFONE: "))
                print("\n\033[92mCliente atualizado com sucesso!\033[0m")

                for pessoa_dados in dados:
                    if pessoa_dados['CPF'] == pessoa['CPF']:
                        pessoa_dados.update(pessoa)
                        escrever_cadastro(dados)
            else:
                print("\n\033[91mNão consegui encontrar esse cadastro\033[0m")
    else:
        print("\n\033[91mCliente não encontrado.\n\033[0m")
        
    input("\nPressione Enter para voltar...")
    os.system('cls')