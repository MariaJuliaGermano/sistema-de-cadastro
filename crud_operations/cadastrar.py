import os
from database.data_handler import ler_cadastro, escrever_cadastro


def cadastrar():
    os.system('cls')
    dados = ler_cadastro()
    print("\n\033[93mCadastrando um cliente:\033[0m\n")
    nome = input("Nome: ")
    email = input("E-mail: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")

    novo_cadastro = {
        "NOME": nome,
        "EMAIL": email,
        "CPF": cpf,
        "TELEFONE": telefone
    }

    dados.append(novo_cadastro)
    escrever_cadastro(dados)

    print("\n\033[92mCliente Cadastrado com sucesso!\033[0m\n")
    input("\nPressione Enter para voltar...")
    os.system('cls')