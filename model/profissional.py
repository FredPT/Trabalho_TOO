class Profissional:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade
        self.__servicos = []

    def __str__(self):
        return f"Profissional: {self.__nome} ({self.__especialidade})"
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.strip()

    @property
    def especialidade(self):
        return self.__especialidade
    
    @especialidade.setter
    def especialidade(self, nova_especialidade):
        self.__especialidade = nova_especialidade.strip()

    @property
    def servicos(self):
        return self.__servicos
    
    def adicionarServico(self, servico):
        self.__servicos.append(servico)
    
    def podeRealizar(self, servico):
        return any(s.nome == servico.nome for s in self.__servicos)
    
    def exibir_dados(self):
        dados = f"Profissional cadastrado:\n"
        dados += f"  Nome: {self.__nome}\n"
        dados += f"  Especialidade: {self.__especialidade}\n"
        dados += f"  Serviços oferecidos: {len(self.__servicos)}\n"
        if self.__servicos:
            dados += f"  Lista de serviços: {', '.join([s.nome for s in self.__servicos])}\n"
        return dados