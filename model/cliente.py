from typing import List

class Cliente:
    def __init__(self, nome: str, telefone: str):
        self.nome = nome
        self.telefone = telefone
        self.historico: List = []
    
    def adicionarAgendamento(self, agendamento):
        self.historico.append(agendamento)
    
    def listarHistorico(self) -> List:
        return self.historico