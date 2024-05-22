import json

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
    nome = str(input("Digite o seu nome: "))
    idade = int(input("Digite a sua idade: "))
    email = str(input("Digite o seu e-mail: "))

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    with open("atividadejson.json", "w") as arquivo:
        json.dump(usuario, arquivo, indent=4)

def listar():
    with open("atividadejson.json", "r") as arquivo:
        dados = json.load(arquivo)
    print(dados)

def excluir():
    nome = input("Digite o nome da pessoa que deseja excluir: ").lower()
    with open('atividadejson.json', 'r') as arquivo:
        dados = json.load(arquivo)

    for pessoa in dados:
        if dados['nome'] == nome:
            dados.remove(pessoa)

def main():
    nome_sistema()
    while True:
        menu()
        escolha()

if __name__ == "__main__":
    main()