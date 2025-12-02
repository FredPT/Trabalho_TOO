from datetime import datetime

class Agendamento:
    def __init__(self, dataHora, cliente, profissional, servico):
        self.__dataHora = dataHora
        self.__cliente = cliente
        self.__profissional = profissional
        self.__servico = servico
        self.__valorFinal = 0.0

    def __str__(self):
        data_formatada = self.__dataHora.strftime("%d/%m/%Y %H:%M")
        return f"[Agendamento] {self.__cliente.nome} - {self.__servico.nome} - {data_formatada}"

    @property
    def dataHora(self):
        return self.__dataHora
    
    @dataHora.setter
    def dataHora(self, nova_data):
        if isinstance(nova_data, datetime):
            self.__dataHora = nova_data
        else:
            raise ValueError("Data deve ser um objeto datetime")

    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, novo_cliente):
        self.__cliente = novo_cliente

    @property
    def profissional(self):
        return self.__profissional
    
    @profissional.setter
    def profissional(self, novo_profissional):
        self.__profissional = novo_profissional

    @property
    def servico(self):
        return self.__servico
    
    @servico.setter
    def servico(self, novo_servico):
        self.__servico = novo_servico

    @property
    def valorFinal(self):
        return self.__valorFinal
    
    @valorFinal.setter
    def valorFinal(self, novo_valor):
        self.__valorFinal = novo_valor
    
    def calcularValor(self, estrategia):
        self.__valorFinal = estrategia.calcular(self.__servico.preco)
        return self.__valorFinal
    
    def exibir_dados(self):
        dados = f"\nAgendamento cadastrado:\n"
        dados += f"  Cliente: {self.__cliente.nome}\n"
        dados += f"  Profissional: {self.__profissional.nome}\n"
        dados += f"  Serviço: {self.__servico.nome}\n"
        dados += f"  Data/Hora: {self.__dataHora.strftime('%d/%m/%Y %H:%M')}\n"
        dados += f"  Valor Final: R$ {self.__valorFinal:.2f}\n"
        return dados