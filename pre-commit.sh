#!/bin/bash

echo "Executando o projeto antes do commit..."
python main.py

if [ $? -ne 0 ]; then
  echo "O projeto encontrou um erro durante a execução. Commit cancelado."
  exit 1
fi

echo "O projeto foi executado com sucesso. Continuando com o commit."
