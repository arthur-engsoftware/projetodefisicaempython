#!/bin/bash
# Este script deixa mais facil rodar o projeto: ele confere se as
# bibliotecas necessarias (numpy e matplotlib) estao instaladas e,
# se nao estiverem, instala automaticamente. Depois roda o programa.
#
# Como usar (no terminal, dentro desta pasta):
#   ./executar.sh
#
# Se der erro de permissao, rode antes:
#   chmod +x executar.sh

echo "Verificando bibliotecas necessarias..."

python3 -c "import numpy, matplotlib" 2>/dev/null

if [ $? -ne 0 ]; then
    echo "Instalando numpy e matplotlib (pode levar alguns segundos)..."
    pip3 install -r requirements.txt

    if [ $? -ne 0 ]; then
        echo "Tentando novamente com --break-system-packages..."
        pip3 install -r requirements.txt --break-system-packages
    fi
fi

echo "Iniciando o programa..."
echo ""
python3 projeto_vetores.py
