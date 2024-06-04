from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.imovel_entity import ImovelEntity

class IImoveisRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ImovelEntity]:
        pass
    @abstractmethod
    def get_sum_price_by_district(self) -> List[dict[str, float]]:
        pass
