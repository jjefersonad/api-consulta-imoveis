def setup_routes(app):
    from app.interfaces.api.controllers.imoveis_controller import imoveis_controller
    app.register_blueprint(imoveis_controller, url_prefix='/api/v1')