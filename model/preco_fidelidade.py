from model.price_strategy import PriceStrategy

class PrecoFidelidade(PriceStrategy):
    def calcular(self, preco_base):
        return preco_base * 0.9  # 10% desconto