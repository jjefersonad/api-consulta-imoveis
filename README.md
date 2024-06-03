# Projeto Flask API
Projeto API de consulta de imóveis

## Versão do Python
```
Python 3.11.0
```

## Iniciar o ambiente virtual
```
source venv/bin/activate
```

## Para adicionar novas dependencias
```
./add_package.sh <nome_dependencia>
```

## Para configurar acesso ao banco
Definir a variável `DATABASE_URL` igual ao exemplo do arquivo `.env_example`
```
DATABASE_URL='postgresql://conexao:conexao@localhost/dashboard'
```

## Comandos para rodar migrations
```
flask db init 
flask db migrate -m "Create initial migration"
flask db upgrade
```

## Para criar uma nova tabela
Tem que adicionar a importação da nova entidade no aquivo `app/core/entities/__init__.py`
Rodar o comando:
```
flask db migrate -m "<descrição da nova entidade>"
```

## Pata aplicar as novas migrations
```
flask db upgrade
```

