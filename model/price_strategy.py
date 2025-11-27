from abc import ABC, abstractmethod

class PriceStrategy(ABC):
    @abstractmethod
    def calcular(self, preco_base: float) -> float:
        pass