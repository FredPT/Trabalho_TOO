from model.price_strategy import PriceStrategy

class PrecoNormal(PriceStrategy):
    def calcular(self, preco_base: float) -> float:
        return preco_base