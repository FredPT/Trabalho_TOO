from model.price_strategy import PriceStrategy

class PrecoPromocional(PriceStrategy):
    def calcular(self, preco_base: float) -> float:
        return preco_base * 0.8  # 20% desconto