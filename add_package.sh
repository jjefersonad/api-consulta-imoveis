#!/bin/bash

# Ativar o ambiente virtual
source venv/bin/activate

# Instalar um pacote
pip install "$1"

# Atualizar o requirements.txt
pip freeze > requirements.txt

# Desativar o ambiente virtual
deactivate