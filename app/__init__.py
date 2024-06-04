import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.infra.config.config import DevelopmentConfig
from app.interfaces.api.routes import setup_routes
from flask_cors import CORS

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = SQLAlchemy()
migrate = Migrate()

# importando as entidades
from app.core.entities import *

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)

    # Verificar se a conexão com o banco de dados foi estabelecida
    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
        try:
            db.create_all()
            logger.info('Conexão com o banco de dados estabelecida com sucesso.')
        except Exception as e:
            logger.error('Erro ao conectar ao banco de dados: %s', e)

    # Definindo rotas
    setup_routes(app)

    return app