# Sistema de Cadastro de Clientes

Este é um sistema simples de cadastro de clientes, implementado em Python, que oferece funcionalidades de **Cadastrar**, **Exibir**, **Buscar**, **Atualizar** e **Excluir** clientes. O sistema utiliza um arquivo JSON como banco de dados para armazenar as informações dos clientes.

## Funcionalidades

1. **Cadastrar Clientes**: Adiciona novos clientes ao sistema.
2. **Exibir Clientes**: Exibe todos os clientes cadastrados no sistema.
3. **Buscar Cliente**: Pesquisa clientes pelo nome.
4. **Atualizar Cliente**: Atualiza as informações de um cliente existente.
5. **Excluir Cliente**: Remove um cliente do sistema.
6. **Sair**: Encerra o sistema.

## Estrutura do Projeto

```plaintext
├── crud_operations/
│   ├── atualizar.py
│   ├── buscar.py
│   ├── cadastrar.py
│   ├── excluir.py
│   └── exibir.py
├── storage/
│   └── data_handler.py
├── cadastro.json
└── index.py
