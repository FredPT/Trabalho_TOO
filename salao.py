from typing import List
from datetime import datetime
from cliente import Cliente
from profissional import Profissional
from agendamento import Agendamento
from service import Service, ServiceFactory, PriceStrategy, PrecoNormal

class Salao:
    def __init__(self):
        self.clientes: List[Cliente] = []
        self.profissionais: List[Profissional] = []
    
    def cadastrarCliente(self, nome: str, telefone: str) -> Cliente:
        cliente = Cliente(nome, telefone)
        self.clientes.append(cliente)
        return cliente
    
    def cadastrarProfissional(self, nome: str, especialidade: str) -> Profissional:
        profissional = Profissional(nome, especialidade)
        self.profissionais.append(profissional)
        return profissional
    
    def agendar(self, dataHora: datetime, cliente: Cliente, profissional: Profissional, 
                tipo_servico: str, estrategia: PriceStrategy = None) -> Agendamento:
        servico = ServiceFactory.criarServico(tipo_servico)
        
        if not profissional.podeRealizar(servico):
            raise ValueError(f"Profissional {profissional.nome} não pode realizar o serviço {servico.nome}")
        
        agendamento = Agendamento(dataHora, cliente, profissional, servico)
        
        if estrategia is None:
            estrategia = PrecoNormal()
        
        agendamento.calcularValor(estrategia)
        cliente.adicionarAgendamento(agendamento)
        
        return agendamento
    
    def listarProfissionais(self) -> List[Profissional]:
        return self.profissionais