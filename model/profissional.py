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
        for s in self.__servicos:
            if s.nome == servico.nome:
                return True
        return False
    
    def exibir_dados(self):
        dados = f"Profissional cadastrado:\n"
        dados += f"  Nome: {self.__nome}\n"
        dados += f"  Especialidade: {self.__especialidade}\n"
        dados += f"  Serviços oferecidos: {len(self.__servicos)}\n"
        if self.__servicos:
            nomes_servicos = []
            for s in self.__servicos:
                nomes_servicos.append(s.nome)
            dados += f"  Lista de serviços: {', '.join(nomes_servicos)}\n"
        return dados