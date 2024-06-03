from app.core.repositories.imoveis_repository import ImoveisRepository
from flask import jsonify

class ListImoveisUseCase:
  def __init__(self, imoveis_repository: ImoveisRepository):
      self.imoveis_repository = imoveis_repository
  
  def execute(self):
      list = self.imoveis_repository.get_all()
      return jsonify([imovel.to_dict() for imovel in list])
      
  def to_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}
