from abc import ABC, abstractmethod

class Service:
    def __init__(self, nome: str, duracao: int, preco: float):
        self.__nome = nome
        self.__duracao = duracao
        self.__preco = preco

    def __str__(self):
        return f"Serviço: {self.__nome} - {self.__duracao}min - R$ {self.__preco:.2f}"
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.strip()

    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self, nova_duracao):
        if 0 < nova_duracao < 500:
            self.__duracao = nova_duracao
        else:
            print("Valor para duração inválido!!")

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            print("Valor para preço inválido!!")
    
    def exibir_dados(self):
        dados = f"Serviço: {self.__nome}\n"
        dados += f"Duração: {self.__duracao} minutos\n"
        dados += f"Preço: R$ {self.__preco:.2f}\n"
        return dados

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