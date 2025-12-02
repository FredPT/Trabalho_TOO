from model.cliente import Cliente
from model.profissional import Profissional
from model.agendamento import Agendamento
from model.preco_normal import PrecoNormal
from model.servicefactory import ServiceFactory

class Salao:
    def __init__(self):
        self.__clientes = []
        self.__profissionais = []

    def __str__(self):
        return f"Salão - {len(self.__clientes)} clientes, {len(self.__profissionais)} profissionais"
    
    @property
    def clientes(self):
        return self.__clientes
    
    @property
    def profissionais(self):
        return self.__profissionais
    
    def cadastrarCliente(self, nome, telefone):
        cliente = Cliente(nome, telefone)
        self.__clientes.append(cliente)
        return cliente
    
    def cadastrarProfissional(self, nome, especialidade):
        profissional = Profissional(nome, especialidade)
        self.__profissionais.append(profissional)
        return profissional
    
    def agendar(self, dataHora, cliente, profissional, 
                tipo_servico, estrategia=None):
        servico = ServiceFactory.criarServico(tipo_servico)
        
        if not profissional.podeRealizar(servico):
            raise ValueError(f"Profissional {profissional.nome} não pode realizar o serviço {servico.nome}")
        
        agendamento = Agendamento(dataHora, cliente, profissional, servico)
        
        if estrategia is None:
            estrategia = PrecoNormal()
        
        agendamento.calcularValor(estrategia)
        cliente.adicionarAgendamento(agendamento)
        
        return agendamento
    
    def listarProfissionais(self):
        return self.__profissionais
    
    def exibir_dados(self):
        dados = f"Salão de Beleza:\n"
        dados += f"  Total de clientes: {len(self.__clientes)}\n"
        dados += f"  Total de profissionais: {len(self.__profissionais)}\n"
        return dados