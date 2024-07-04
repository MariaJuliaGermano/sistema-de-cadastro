import json

def ler_cadastro():
    try:
        with open('cadastro.json', 'r') as arquivo:
            dados = json.load(arquivo)
            if not isinstance(dados, list):
                raise ValueError("Conteúdo do arquivo não é uma lista válida de dicionários")
            for item in dados:
                if not isinstance(item, dict):
                    raise ValueError("Conteúdo do arquivo não é uma lista válida de dicionários")
            return dados
    except (FileNotFoundError, ValueError):
        return []
    except json.JSONDecodeError:
        return []

def escrever_cadastro(dados):
    try:
        with open('cadastro.json', 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

def nome_sistema():
    print("-=" * 11)
    print("Cadastro de Clientes")

def menu():
    print("-=" * 11)
    print("1. Cadastrar Clientes")
    print("2. Exibir Clientes")
    print("3. Buscar Cliente")
    print("4. Atualizar Cliente")
    print("5. Excluir Cliente")
    print("6. Sair")

def cadastrar():
    try:
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
        escrever_cadastro(dados)

        print("\n\033[92mCliente Cadastrado com sucesso!\033[0m\n")
    except Exception as e:
        print(f"Erro ao cadastrar cliente: {e}")

def main():
    try:
        nome_sistema()
        while True:
            menu()
            escolha = input("\nDigite a sua opção: ")
            if escolha == '1':
                cadastrar()
            elif escolha == '2':
                print("Opção 2 escolhida")
                # Implemente a função de exibir clientes aqui
            elif escolha == '3':
                print("Opção 3 escolhida")
                # Implemente a função de buscar cliente aqui
            elif escolha == '4':
                print("Opção 4 escolhida")
                # Implemente a função de atualizar cliente aqui
            elif escolha == '5':
                print("Opção 5 escolhida")
                # Implemente a função de excluir cliente aqui
            elif escolha == '6':
                print("\n\033[93mSaindo do sistema...")
                print("Obrigado, volte sempre!\033[0m")
                break
            else:
                print("\033[91mOpção inválida. Tente novamente!\033[0m")
    except Exception as e:
        print(f"Erro no sistema: {e}")

if __name__ == "__main__":
    main()
