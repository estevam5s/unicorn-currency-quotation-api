[![Get professional and fast support](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/unicorn-binance-suite/master/images/support/LUCIT-get-professional-and-fast-support.png)]()

[![GitHub Release](https://img.shields.io/github/release/LUCIT-Systems-and-Development/unicorn-binance-suite.svg?label=github)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/LUCIT-Systems-and-Development/unicorn-binance-suite/total?color=blue)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/releases)
[![Conda Release](https://img.shields.io/conda/vn/conda-forge/unicorn-binance-suite.svg?color=blue)](https://anaconda.org/conda-forge/unicorn-binance-suite)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/unicorn-binance-suite.svg?color=blue)](https://anaconda.org/conda-forge/unicorn-binance-suite)
[![PyPi Release](https://img.shields.io/pypi/v/unicorn-binance-suite?color=blue)](https://pypi.org/project/unicorn-binance-suite/)
[![PyPi Downloads](https://pepy.tech/badge/unicorn-binance-suite)](https://pepy.tech/project/unicorn-binance-suite)
[![License](https://img.shields.io/github/license/LUCIT-Systems-and-Development/unicorn-binance-suite.svg?color=blue)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/blob/master/LICENSE)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/unicorn_binance_suite.svg)](https://www.python.org/downloads/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn_binance_suite.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/issues)
[![Azure Pipelines](https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/unicorn-binance-suite-feedstock?branchName=main)](https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=15707&branchName=main)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://unicorn-binance-suite.docs.lucit.tech/)
[![Github](https://img.shields.io/badge/source-github-yellow)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite)
[![Telegram](https://img.shields.io/badge/chat-telegram-yellow)](https://t.me/unicorndevs)
[![Gitter](https://badges.gitter.im/unicorn-binance-suite/unicorn-binance-suite.svg)](https://gitter.im/unicorn-binance-suite/unicorn-binance-suite?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![LUCIT-UBS-Banner](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/unicorn-binance-suite/master/images/logo/LUCIT-UBS-Banner-Readme.png)]()


# Projeto de Cotação de Moedas

Este projeto consome a API de cotação de moedas (https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL) e exibe as cotações do Dólar, Euro e Bitcoin em relação ao Real brasileiro. O projeto utiliza padrões de projeto SOLID e uma arquitetura MSC (Model-Service-Controller).


## Índice

- [Introdução](#introdução)
- [Tecnologias](#tecnologias)
- [Scripts de inicialização do projeto](#scripts-de-inicialização-do-projeto)
    - [Como iniciar o projeto](#1-como-iniciar-o-projeto)
    - [Instalando dependências do projeto](#2-instalando-dependências-do-projeto)
    - [Usando o Docker](#3-usando-o-docker)
- [Versão do projeto](#versão-do-projeto)
- [Features](#features)
- [Tópicos sobre o projeto](#tópicos-sobre-o-projeto)
- [Descrição](#descrição)
- [Arquitetura do projeto](#arquitetura-do-projeto)
- [Estrutura de pastas e arquivos](#estrutura-de-pastas-e-arquivos)
- [Deploy no Heroku](#deploy-no-heroku)


## Introdução

O objetivo deste projeto é fornecer uma maneira fácil e rápida de obter cotações de moedas, como Dólar, Euro e Bitcoin, em relação ao Real brasileiro. O projeto foi desenvolvido utilizando os princípios SOLID e melhores práticas de engenharia de software.


## Tecnologias

- Python 3.9
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Docker
- docker-compose
- Heroku


## Descrição

O projeto foi desenvolvido com base nos princípios SOLID e padrões de projeto para garantir um código limpo, modular e de fácil manutenção. A arquitetura MSC (Model-Service-Controller) foi adotada para organizar melhor o código e separar as responsabilidades.


## Estrutura de pastas e arquivos

```bash
projeto-cotacao-moedas/
├─ api/
│   ├─ app.py
│   ├─ main.py
│   ├─ data_formatter.py
│   ├─ currency_quotation.py
│   └─ api_request.py
├─ docs/
├─ test/
│   ├─ __init__.py
│   └─ test_main.py
├─ .circleci/
│   └─ config.yml
├─ .dockerignore
├─ .gitignore
├─ .gitmodules
├─ .pre-commit-config.yaml
├─ AUTHORS.md
├─ CHANGELOG.md
├─ CONTRIBUTING.md
├─ README.md
├─ Makefile
├─ docker-compose.yaml
├─ docker-compose-test.yaml
├─ docker-compose.deploy.yml
├─ configuration.py
├─ package.json
├─ requirements.txt
├─ setup.cfg
├─ pylintrc
└─ .coafile
```


## Configuração do ambiente

### Ambiente virtual e instalação de dependências

Para isolar as dependências do projeto, é recomendado utilizar um ambiente virtual. O projeto foi configurado para usar o venv. Para criar e ativar o ambiente virtual, execute os comandos a seguir no terminal:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências do projeto executando o seguinte comando:

```bash
pip install -r requirements.txt
```


### Variáveis de ambiente

O projeto utiliza variáveis de ambiente para armazenar informações sensíveis e configurações específicas. Para configurar as variáveis de ambiente, crie um arquivo .env na raiz do projeto e preencha-o com as variáveis apropriadas. Um exemplo de arquivo .env pode ser encontrado abaixo:

```makefile
FLASK_APP=api/app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
```


## Scripts de inicialização do projeto

### 1. Como iniciar o projeto

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/seuusuario/projeto-cotacao-moedas.git
cd projeto-cotacao-moedas
```

### 2. Instalando dependências do projeto

Crie um ambiente virtual e instale as dependências:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Usando o Docker

Para iniciar o projeto com Docker, primeiro instale o Docker e docker-compose. Em seguida, execute o seguinte comando:

```bash
docker-compose up
```

### Testes

Os testes do projeto estão localizados na pasta test. Para executar os testes, certifique-se de que você está no ambiente virtual e execute o seguinte comando:

```bash
python -m unittest discover test
```

### Logging

O projeto possui logs configurados para auxiliar no monitoramento e depuração. Os arquivos de log são armazenados na pasta log na raiz do projeto.

## Autenticação e autorização

O projeto utiliza o Flask-Login para lidar com a autenticação e autorização de usuários. As credenciais dos usuários são armazenadas em um banco de dados. Para configurar o banco de dados, siga as instruções na seção "Variáveis de ambiente".

### Uso do Docker

O projeto inclui arquivos Dockerfile e docker-compose.yml para facilitar a implantação e execução do projeto usando o Docker. Para construir a imagem do Docker, execute o seguinte comando na raiz do projeto:

```bash
docker build -t cotacao-moedas .
```

Em seguida, execute o projeto usando o `docker-compose`:

```bash
docker-compose up
```

## Integração contínua e entrega contínua (CI/CD)

O projeto utiliza o CircleCI e o Travis CI para automatizar a integração e entrega contínua. Os arquivos de configuração estão localizados na pasta `.circleci` e na raiz do projeto (`.travis.yml`), respectivamente.

## Contribuição

Consulte o arquivo `CONTRIBUTING.md` para obter informações sobre como contribuir para o projeto, incluindo convenções de código e fluxo de trabalho.


## Autores

Os autores e colaboradores do projeto estão listados no arquivo `AUTHORS.md`.


## Arquitetura do projeto

A arquitetura do projeto é baseada no padrão MSC (Model-Service-Controller), que organiza o código em três camadas principais: Model, Service e Controller. A camada Model lida com a lógica de negócios e a persistência de dados, a camada Service encapsula a lógica de negócios e a comunicação entre as camadas Model e Controller, e a camada Controller é responsável por gerenciar as solicitações e respostas HTTP.


## Versão do projeto

Versão atual: 1.0.0


## Features

- Consumo da API de cotação de moedas
- Exibição das cotações no console e na aplicação Flask
- Autenticação e autorização
- Testes unitários
- Integração contínua com Travis CI e CircleCI
- Deploy no Heroku


## Tópicos sobre o projeto

- Implementação dos princípios SOLID

  * Padrões de projeto
  * Arquitetura MSC (Model-Service-Controller)


## Deploy no Heroku

Para fazer o deploy do projeto no Heroku, siga os passos a seguir:

1. Crie uma conta no Heroku (https://signup.heroku.com/).

2. Instale o CLI do Heroku (https://devcenter.heroku.com/articles/heroku-cli).

3. Faça login no CLI do Heroku:

```bash
heroku login
# Digite seu e-mail e senha
```

4. Crie uma nova aplicação no Heroku:
  
```bash
heroku create nome-da-sua-aplicacao

# Exemplo:
heroku create projeto-cotacao-moedas
```

5. Faça o deploy da aplicação no Heroku:

```css
git push heroku main
```

5. Execute a aplicação no Heroku:

```arduino
heroku open
```

Agora você pode acessar a aplicação no navegador através do endereço fornecido pelo Heroku.