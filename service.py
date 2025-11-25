from abc import ABC, abstractmethod

class Service:
    def __init__(self, nome: str, duracao: int, preco: float):
        self.nome = nome
        self.duracao = duracao
        self.preco = preco

class ServiceFactory:
    @staticmethod
    def criarServico(tipo: str) -> Service:
        servicos = {
            "CorteM": Service("Corte Masculino", 30, 25.0),
            "CorteF": Service("Corte Feminino", 45, 40.0),
            "Barba": Service("Barba", 20, 15.0),
            "Pintar": Service("Pintar Cabelo", 120, 80.0),
            "Sobrancelha": Service("Sobrancelha", 15, 20.0)
        }
        return servicos.get(tipo, Service("Serviço Padrão", 30, 30.0))

class PriceStrategy(ABC):
    @abstractmethod
    def calcular(self, preco_base: float) -> float:
        pass

class PrecoNormal(PriceStrategy):
    def calcular(self, preco_base: float) -> float:
        return preco_base

class PrecoPromocional(PriceStrategy):
    def calcular(self, preco_base: float) -> float:
        return preco_base * 0.8  # 20% desconto

class PrecoFidelidade(PriceStrategy):
    def calcular(self, preco_base: float) -> float:
        return preco_base * 0.9  # 10% desconto