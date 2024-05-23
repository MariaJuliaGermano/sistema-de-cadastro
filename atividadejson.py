import json
from time import sleep

def nome_sistema():
    print("="*10, end="")
    print("SISTEMA DE CADASRO", end="")
    print("="*10)


def menu():
    print("-="*7)
    print("1. Cadastrar Cliente")
    print("2. Listar Clientes")
    print("3. Excluir Clientes")
    print("4. Sair")


def escolha():
    escolha = int(input("Escolha uma das opções: "))
    match escolha:
        case 1:
            cadastrar()
        case 2:
            listar()
        case 3:
            excluir()
        case 4:
            print("Obrigada, volte sempre!")
            exit()


def cadastrar():
    nome = str(input("Digite o seu nome: ")).strip()
    idade = int(input("Digite a sua idade: "))
    email = str(input("Digite o seu e-mail: ")).strip()

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    with open("atividade.json", "r") as arquivo:
        usuarios = json.load(arquivo)

    usuarios.append(usuario)

    with open("atividade.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)
        arquivo.write("\n")
    
    print("Cliente Cadastrado com sucesso!")


def listar():
    with open("atividade.json", "r") as arquivo:
        dados = json.load(arquivo)
        if dados:
            print("Listando clientes cadasrtados")
            for linha in dados:
                print(linha)


def excluir():
    nome = input("Digite o nome da pessoa que deseja excluir: ").strip()
    with open('atividade.json', 'r') as arquivo:
        dados = json.load(arquivo)

    for pessoa in dados:
        if pessoa['nome'].lower() == nome.lower():
            dados.remove(pessoa)

    with open("atividade.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
            

def main():
    nome_sistema()
    while True:
        menu()
        escolha()


if __name__ == "__main__":
    main()
