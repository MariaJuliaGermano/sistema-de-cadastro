import os
from time import sleep

cadastro = []


def nome_sistema():
    print("-=" *11)
    print("Cadastro de Clientes")


def menu():
    print("-=" *11)
    print("1. Cadastrar Clientes")
    print("2. Exibir Clientes")
    print("3. Buscar Cliente")
    print("4. Atualizar Cliente")
    print("5. Excluir Cliente")
    print("6. Sair")


def cadastrar():
    global cadastro
    pessoa = dict()
    print("\n\033[93mCadastrando um cliente:\033[0m\n")
    pessoa['NOME'] = str(input("Nome: "))
    pessoa['EMAIL'] = str(input("E-mail: "))
    pessoa['CPF'] = int(input("CPF: "))
    pessoa['TELEFONE'] = int(input("TELEFONE: "))

    cadastro.append(pessoa.copy())

    print("\n\033[92mCliente Cadastrado com sucesso!\033[0m\n")
    sleep(1)


def exibir():
    global cadastro
    if cadastro:
        print("\n\033[93mExibindo clientes cadastrados:\033[0m\n")
        for pessoa in cadastro:
            print("\033[96m===== ",pessoa["NOME"]," =====\033[0m")
            print(f"NOME: {pessoa['NOME']}")
            print(f"EMAIL: {pessoa['EMAIL']}")
            print(f"CPF: {pessoa['CPF']}")
            print(f"TELEFONE: {pessoa['TELEFONE']}\n")
        sleep(2)
    else:
        print("\n\033[91mNão há pessoas cadastradas.\033[0m\n")

    sleep(1)


def buscar():
    global cadastro
    nome = input("\nDigite o nome do cliente que deseja buscar: ")
    encontrado = False
    for pessoa in cadastro:
        if pessoa["NOME"].lower() == nome.lower():
            print("\n\033[93mCliente encontrado:\033[0m\n")
            print("===== ",pessoa["NOME"]," =====")
            print(f"NOME: {pessoa['NOME']}")
            print(f"EMAIL: {pessoa['EMAIL']}")
            print(f"CPF: {pessoa['CPF']}")
            print(f"TELEFONE: {pessoa['TELEFONE']}\n")
            sleep(2)
            encontrado = True
    if not encontrado:
        print("\n\033[91mCliente não encontrado!\033[0m\n")


def atualizar():
    global cadastro
    nome = input("\nDigite o nome do cliente que deseja atualizar: ")
    for pessoa in cadastro:
        if pessoa['NOME'].lower() == nome.lower():
            print("\n\033[93mAtualizando cliente:\033[0m\n")
            print("===== ",pessoa["NOME"]," =====")
            pessoa['NOME'] = input(f"NOME: {pessoa["NOME"]} --> NOVO NOME: ")
            pessoa['EMAIL'] = input(f"EMAIL: {pessoa["EMAIL"]} --> NOVO EMAIL: ")
            pessoa['CPF'] = int(input(f"CPF: {pessoa["CPF"]} --> NOVO CPF: "))
            pessoa['TELEFONE'] = int(input(f"TELEFONE: {pessoa["TELEFONE"]} --> NOVO TELEFONE: "))
            print("\n\033[92mCliente atualizado com sucesso!\033[0m\n")
            return
        
    print("\n\033[91mCliente não encontrado.\n\033[0m")


def excluir():
    global cadastro
    nome = input("\nDigite o nome do cliente que deseja excluir: ")
    for pessoa in cadastro:
        if pessoa['NOME'].lower() == nome.lower():
            cadastro.remove(pessoa)
            print("\n\033[92mCliente excluído com sucesso!\033[0m\n")
            return
        
    print("\n\033[91mCliente não encontrado.\n\033[0m")


def escolha():
    opcao = int(input("\nDigite a sua opção: ")) 
    match opcao:
        case 1:
            cadastrar()
        case 2:
            exibir()
        case 3:
            buscar()
        case 4:
            atualizar()
        case 5:
            excluir()
        case 6:
            print("\n\033[93mSaindo do sistema...")
            sleep(1)
            print("Obrigado, volte sempre!\033[0m")
            exit()
        case __:
            print("\033[91mOpção inválida. Tente novamente!\033[0m")
            escolha()


def main():
    nome_sistema()
    while True:
        menu()
        escolha()


if __name__ == "__main__":
    main()
