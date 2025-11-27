from datetime import datetime
from model.salao import Salao
from model.service import PrecoNormal, PrecoPromocional, PrecoFidelidade
from model.servicefactory import ServiceFactory
from model.corte_masculino import CorteMasculino
from model.corte_feminino import CorteFeminino
from model.barba import Barba
from model.pintar_cabelo import PintarCabelo
from model.sobrancelha import Sobrancelha

def main():
    print("SISTEMA DE GERENCIAMENTO DE SALÃO DE BELEZA\n")
    
    # Criar instância do salão
    salao = Salao()
    print(salao.exibir_dados())
    
    # Cadastrar clientes
    print("CADASTRANDO CLIENTES")
    cliente1 = salao.cadastrarCliente("Frederico", "(51) 99999-9999")
    print(cliente1.exibir_dados())
    
    cliente2 = salao.cadastrarCliente("Vanessa", "(51) 88888-8888")
    print(cliente2.exibir_dados())
    
    # Cadastrar profissionais
    prof1 = salao.cadastrarProfissional("João", "Barbeiro")
    prof2 = salao.cadastrarProfissional("Ana", "Cabeleireira")
    
    # Criar serviços
    # Via Factory
    corte_m = ServiceFactory.criarServico("CorteM")
    corte_f = ServiceFactory.criarServico("CorteF")
    pintar = ServiceFactory.criarServico("Pintar")
    
    # Via Classe Direta
    barba = Barba()
    sobrancelha = Sobrancelha()
    
    # Adicionar serviços aos profissionais
    prof1.adicionarServico(corte_m)
    prof1.adicionarServico(barba)
    prof2.adicionarServico(corte_f)
    prof2.adicionarServico(pintar)
    prof2.adicionarServico(sobrancelha)
    
    print("Profissionais cadastrados com seus serviços:")
    print(prof1.exibir_dados())
    print(prof2.exibir_dados())
    
    # Exibir alguns serviços disponíveis
    print("ALGUNSSERVIÇOS DISPONÍVEIS")
    print(corte_m.exibir_dados())
    print(corte_f.exibir_dados())
    print(barba.exibir_dados())
    print(pintar.exibir_dados())
    
    
    # Realizar agendamentos com diferentes estratégias de preço
    print("REALIZANDO AGENDAMENTOS")
    
    # Agendamento 1 - Preço normal
    agend1 = salao.agendar(
        datetime(2025, 12, 1, 10, 0),
        cliente1,
        prof1,
        "CorteM",
        PrecoNormal()
    )
    print(agend1.exibir_dados())
    
    # Agendamento 2 - Preço promocional
    agend2 = salao.agendar(
        datetime(2025, 12, 3, 14, 0),
        cliente2,
        prof2,
        "CorteF",
        PrecoPromocional()
    )
    print(agend2.exibir_dados())
    
    # Agendamento 3 - Preço fidelidade
    agend3 = salao.agendar(
        datetime(2025, 12, 5, 16, 0),
        cliente1,
        prof1,
        "Barba",
        PrecoFidelidade()
    )
    print(agend3.exibir_dados())
    
    # Agendamento 4 - Sobrancelha com preço normal
    agend4 = salao.agendar(
        datetime(2025, 12, 16, 9, 30),
        cliente2,
        prof2,
        "Sobrancelha"
    )
    print(agend4.exibir_dados())
    
    # Mostrar dados atualizados do salão
    print("STATUS FINAL DO SALÃO")
    print(salao.exibir_dados())
    
    # Mostrar histórico atualizado dos clientes
    print("HISTÓRICO DE CLIENTES")
    print(cliente1.exibir_dados())
    print(cliente2.exibir_dados())
    

    # Modificação de agendamento
    print("Modificando agendamento:")
    print(f"Data original: {agend1.dataHora.strftime('%d/%m/%Y %H:%M')}")
    agend1.dataHora = datetime(2025, 12, 1, 11, 0)
    print(f"Nova data: {agend1.dataHora.strftime('%d/%m/%Y %H:%M')}")
    
    # Modificação de cliente
    print("\nModificando dados do cliente:")
    print(f"Nome original: {cliente1.nome}")
    cliente1.nome = "Frederico P Taufer"
    print(f"Nome modificado: {cliente1.nome}")
    
    # Modificação de profissional
    print("\nModificando dados do profissional:")
    print(f"Especialidade original: {prof1.especialidade}")
    prof1.especialidade = "Barbeiro Especialista"
    print(f"Especialidade modificada: {prof1.especialidade}")
    


if __name__ == "__main__":
    main()