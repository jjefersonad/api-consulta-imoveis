from typing import List, Dict
from app.core.entities.imovel import Imovel
from app.domain.entities.imovel_entity import ImovelEntity
from app.domain.reporitories.imoveis_repository import IImoveisRepository
from app.infra.config.logger import Logger
from app import db
from sqlalchemy import func

class ImoveisRepository(IImoveisRepository):
    def __init__(self):
        self.logger = Logger()
    def get_all(self) -> List[ImovelEntity]:
        self.logger.info('antes da chamada')
        lista_imoveis = Imovel.query.all()
        self.logger.info('depois da chamada')
        return [imovel.to_dict() for imovel in lista_imoveis]
    def get_sum_price_by_district(self) -> List[Dict[str, float]]:
        self.logger.info('antes da chamada')
        
        results = db.session.query(
            Imovel.district,
            func.sum(1).label('total_imoveis'),
            func.sum(Imovel.price).label('total_price')
        ).group_by(Imovel.district).all()
        
        self.logger.info('depois da chamada')
        
        sum_by_district = [{'district': result.district, 'total_price': result.total_price, 'total_imoveis': result.total_imoveis} for result in results]
        return sum_by_district
    