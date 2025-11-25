from typing import List
from service import Service

class Profissional:
    def __init__(self, nome: str, especialidade: str):
        self.nome = nome
        self.especialidade = especialidade
        self.servicos: List[Service] = []
    
    def adicionarServico(self, servico: Service):
        self.servicos.append(servico)
    
    def podeRealizar(self, servico: Service) -> bool:
        return any(s.nome == servico.nome for s in self.servicos)