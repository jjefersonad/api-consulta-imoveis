from app.infra.repositories.imoveis_repository import ImoveisRepository
from flask import jsonify

class TotalPriceForDistrictUseCase:
  def __init__(self, imoveis_repository: ImoveisRepository):
      self.imoveis_repository = imoveis_repository
  
  def execute(self):
      list = self.imoveis_repository.get_sum_price_by_district()
      return jsonify(list)
