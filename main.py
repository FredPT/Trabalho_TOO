from datetime import datetime
from salao import Salao
from service import ServiceFactory, PrecoNormal, PrecoPromocional, PrecoFidelidade

def main():
    # Criar instância do salão
    salao = Salao()
    
    # Cadastrar clientes
    cliente1 = salao.cadastrarCliente("João Silva", "(11) 99999-9999")
    cliente2 = salao.cadastrarCliente("Maria Santos", "(11) 88888-8888")
    
    # Cadastrar profissionais
    prof1 = salao.cadastrarProfissional("Carlos", "Barbeiro")
    prof2 = salao.cadastrarProfissional("Ana", "Cabeleireira")
    
    # Adicionar serviços aos profissionais
    corte_m = ServiceFactory.criarServico("CorteM")
    barba = ServiceFactory.criarServico("Barba")
    corte_f = ServiceFactory.criarServico("CorteF")
    pintar = ServiceFactory.criarServico("Pintar")
    
    prof1.adicionarServico(corte_m)
    prof1.adicionarServico(barba)
    prof2.adicionarServico(corte_f)
    prof2.adicionarServico(pintar)
    
    # Realizar agendamentos com diferentes estratégias de preço
    print("=== SISTEMA DE GERENCIAMENTO DE SALÃO DE BELEZA ===")
    print()
    
    # Agendamento 1 - Preço normal
    agend1 = salao.agendar(
        datetime(2024, 12, 15, 10, 0),
        cliente1,
        prof1,
        "CorteM",
        PrecoNormal()
    )
    print(f"Agendamento 1: {cliente1.nome} - {agend1.servico.nome} - R$ {agend1.valorFinal:.2f}")
    
    # Agendamento 2 - Preço promocional
    agend2 = salao.agendar(
        datetime(2024, 12, 15, 14, 0),
        cliente2,
        prof2,
        "CorteF",
        PrecoPromocional()
    )
    print(f"Agendamento 2: {cliente2.nome} - {agend2.servico.nome} - R$ {agend2.valorFinal:.2f} (Promocional)")
    
    # Agendamento 3 - Preço fidelidade
    agend3 = salao.agendar(
        datetime(2024, 12, 15, 16, 0),
        cliente1,
        prof1,
        "Barba",
        PrecoFidelidade()
    )
    print(f"Agendamento 3: {cliente1.nome} - {agend3.servico.nome} - R$ {agend3.valorFinal:.2f} (Fidelidade)")
    
    print()
    print("=== HISTÓRICO DE CLIENTES ===")
    
    # Mostrar histórico do cliente 1
    print(f"\nHistórico de {cliente1.nome}:")
    for agend in cliente1.listarHistorico():
        print(f"  - {agend.dataHora.strftime('%d/%m/%Y %H:%M')} - {agend.servico.nome} - R$ {agend.valorFinal:.2f}")
    
    # Mostrar histórico do cliente 2
    print(f"\nHistórico de {cliente2.nome}:")
    for agend in cliente2.listarHistorico():
        print(f"  - {agend.dataHora.strftime('%d/%m/%Y %H:%M')} - {agend.servico.nome} - R$ {agend.valorFinal:.2f}")
    
    print()
    print("=== PROFISSIONAIS CADASTRADOS ===")
    for prof in salao.listarProfissionais():
        print(f"- {prof.nome} ({prof.especialidade})")
        print(f"  Serviços: {[s.nome for s in prof.servicos]}")

if __name__ == "__main__":
    main()