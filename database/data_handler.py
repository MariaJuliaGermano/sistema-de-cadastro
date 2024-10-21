import json

def ler_cadastro():
    try:
        with open('database/cadastro.json', 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, ValueError):
        return []
    except json.decoder.JSONDecodeError:
        return []


def escrever_cadastro(dados):
    with open('database/cadastro.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
        