from flask import Blueprint, request, jsonify
from app.core.use_cases.list_imoveis import ListImoveisUseCase
from app.core.repositories.imoveis_repository import ImoveisRepository

imoveis_controller = Blueprint('imoveis_controller', __name__)

@imoveis_controller.route('/imoveis', methods=['GET'])
def list_imoveis():
  #data = request.get_json()
  # price, condo, size, rooms, toilets, suites, parking, elevator, furnished, swimming_pool, new, district, negotiation_type, property_type, latitude, longitude
  repository = ImoveisRepository()
  usecase = ListImoveisUseCase(repository)
  # list = usecase.execute()

  return usecase.execute(), 201