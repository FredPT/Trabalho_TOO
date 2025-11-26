from typing import List

class Cliente:
    def __init__(self, nome: str, telefone: str):
        self.nome = nome
        self.telefone = telefone
        self.__historico: List = []

    def __str__(self):
        return f"Cliente: {self.__nome} - {self.__telefone}"
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.strip()

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone.strip()

    @property
    def historico(self):
        return self.__historico
    
    def adicionarAgendamento(self, agendamento):
        self.__historico.append(agendamento)
    
    def listarHistorico(self) -> List:
        return self.__historico
    
    def exibir_dados(self):
        dados = f"Cliente cadastrado:\n"
        dados += f"  Nome: {self.__nome}\n"
        dados += f"  Telefone: {self.__telefone}\n"
        dados += f"  Total de agendamentos: {len(self.__historico)}\n"
        return dados