# Documentação do Projeto: Sistema de Gerenciamento de Farmácia

## Sumário

1. [Descrição do Projeto](#descrição-do-projeto)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Instalação](#instalação)
4. [Estrutura do Projeto](#estrutura-do-projeto)
5. [Uso](#uso)
6. [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
7. [Licença](#licença)

## Descrição do Projeto

O projeto é uma aplicação de linha de comando desenvolvida para gerenciar o estoque e as vendas de uma farmácia. Através de um sistema modular, o usuário pode realizar operações de CRUD (Create, Read, Update, Delete) em diferentes entidades, como funcionários, clientes, produtos e pedidos.

## Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Banco de Dados**: PostgreSQL

## Instalação

Para executar o projeto localmente, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/jeanmcorreia/projeto-farmacia-lab2.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd projeto-farmacia-lab2
   ```
3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Windows use `venv\Scripts\activate`
   ```
4. Instale as dependências necessárias, se houver:
   ```bash
   pip install -r requirements.txt
   ```
5. Configure o banco de dados conforme a documentação na pasta `config`.
6. Execute a aplicação:
   ```bash
   python main.py
   ```

## Estrutura do Projeto

```
projeto-farmacia-lab2/
│
├── main.py                # Executa a aplicação
├── config/                # Configurações e conexão com o banco de dados
│   ├── db.py
├── login/                # Funções de autenticação e cadastro de usuários
│   ├── autenticar.py
│   └── cadastrar.py
├── pessoas/               # Módulo para gerenciamento de funcionários e clientes
│   ├── crud_funcionarios.py
│   └── crud_clientes.py
├── pedidos/               # Módulo para gerenciamento de pedidos
│   └── crud_pedidos.py
├── estoque/               # Módulo para gerenciamento de estoque
│   └── crud_estoque.py
└── produtos/              # Módulo para gerenciamento de produtos
    └── crud_produtos.py
```

## Uso

A aplicação é executada pelo terminal e permite as seguintes operações:

- **Gerenciamento de Funcionários e Clientes**: CRUD para adicionar, visualizar, editar e remover registros.
- **Gerenciamento de Produtos**: CRUD para produtos disponíveis no estoque.
- **Gerenciamento de Pedidos**: Registro e consulta de pedidos realizados.

## Configuração do Banco de Dados

O banco de dados utilizado é o PostgreSQL. As configurações de conexão devem ser ajustadas na pasta `config`. Certifique-se de que o banco de dados esteja acessível e que as credenciais estejam corretas.