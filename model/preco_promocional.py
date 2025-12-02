from model.price_strategy import PriceStrategy

class PrecoPromocional(PriceStrategy):
    def calcular(self, preco_base):
        return preco_base * 0.8  # 20% desconto