from typing import List
from datetime import datetime
from model.cliente import Cliente
from model.profissional import Profissional
from model.agendamento import Agendamento
from model.service import Service
from model.price_strategy import PriceStrategy
from model.preco_normal import PrecoNormal
from model.servicefactory import ServiceFactory

class Salao:
    def __init__(self):
        self.__clientes: List[Cliente] = []
        self.__profissionais: List[Profissional] = []

    def __str__(self):
        return f"Salão - {len(self.__clientes)} clientes, {len(self.__profissionais)} profissionais"
    
    @property
    def clientes(self):
        return self.__clientes
    
    @property
    def profissionais(self):
        return self.__profissionais
    
    def cadastrarCliente(self, nome: str, telefone: str) -> Cliente:
        cliente = Cliente(nome, telefone)
        self.__clientes.append(cliente)
        return cliente
    
    def cadastrarProfissional(self, nome: str, especialidade: str) -> Profissional:
        profissional = Profissional(nome, especialidade)
        self.__profissionais.append(profissional)
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
        return self.__profissionais
    
    def exibir_dados(self):
        dados = f"Salão de Beleza:\n"
        dados += f"  Total de clientes: {len(self.__clientes)}\n"
        dados += f"  Total de profissionais: {len(self.__profissionais)}\n"
        return dados