from time import sleep
from crud_operations.cadastrar import cadastrar
from crud_operations.exibir import exibir
from crud_operations.buscar import buscar
from crud_operations.atualizar import atualizar
from crud_operations.excluir import excluir


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
