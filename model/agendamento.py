from datetime import datetime
from model.cliente import Cliente
from model.profissional import Profissional
from model.service import Service, PriceStrategy

class Agendamento:
    def __init__(self, dataHora: datetime, cliente: Cliente, profissional: Profissional, servico: Service):
        self.dataHora = dataHora
        self.cliente = cliente
        self.profissional = profissional
        self.servico = servico
        self.valorFinal = 0.0
    
    def calcularValor(self, estrategia: PriceStrategy) -> float:
        self.valorFinal = estrategia.calcular(self.servico.preco)
        return self.valorFinal