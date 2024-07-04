import os
import json
from time import sleep


def ler_cadastro():
    try:
        with open('cadastro.json', 'r') as arquivo:
            dados = json.load(arquivo)
            if not isinstance(dados, list):
                raise ValueError
            for item in dados:
                if not isinstance(item, dict):
                    raise ValueError
            return dados
    except (FileNotFoundError, ValueError):
        return []
    except json.JSONDecodeError:
        return []


def escrever_cadastro(dados):
    with open('cadastro.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)


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
    dados = ler_cadastro()
    print("\n\033[93mCadastrando um cliente:\033[0m\n")
    nome = input("Nome: ")
    email = input("E-mail: ")
    cpf = input("CPF: ")
    telefone = input("TELEFONE: ")

    novo_cadastro = {
        "NOME": nome,
        "EMAIL": email,
        "CPF": cpf,
        "TELEFONE": telefone
    }

    dados.append(novo_cadastro)
    escrever_cadastro(novo_cadastro)

    print("\n\033[92mCliente Cadastrado com sucesso!\033[0m\n")
    sleep(1)


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
        sleep(2)
    else:
        print("\n\033[91mNão há pessoas cadastradas.\033[0m\n")

    sleep(1)


def buscar():
    dados = ler_cadastro()
    nome = input("\nDigite o nome do cliente que deseja buscar: ")
    encontrado = False
    for pessoa in dados:
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
    dados = ler_cadastro()
    nome = input("\nDigite o nome do cliente que deseja atualizar: ")
    for pessoa in dados:
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
    dados = ler_cadastro()
    nome = input("\nDigite o nome do cliente que deseja excluir: ")
    for pessoa in dados:
        if pessoa['NOME'].lower() == nome.lower():
            dados.remove(pessoa)
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
