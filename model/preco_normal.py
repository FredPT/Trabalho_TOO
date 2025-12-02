from model.price_strategy import PriceStrategy

class PrecoNormal(PriceStrategy):
    def calcular(self, preco_base):
        return preco_base