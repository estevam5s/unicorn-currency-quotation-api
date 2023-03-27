#!/bin/bash

# Ativar o ambiente virtual
source venv/bin/activate

# Instalar as dependências do projeto (somente na primeira execução ou quando houver mudanças nas dependências)
pip install -r requirements.txt

# Executar o projeto
python main.py
