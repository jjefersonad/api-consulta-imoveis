from app.core.entities.imovel import Imovel

class ImoveisRepository:
    def create(self, imovel: Imovel):
        # Implementar a lógica de persistência de usuário
        pass
    
    def get_all(self):
        return Imovel.query.all()