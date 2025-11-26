# Estrutura do Sistema de Gerenciamento de Salão de Beleza

## Estrutura de Arquivos

```
Trabalho_Final/
├── model/
│   ├── __init__.py
│   ├── service.py          # Service, PriceStrategy
│   ├── servicefactory.py   # ServiceFactory
│   ├── cliente.py          # Cliente
│   ├── profissional.py     # Profissional
│   ├── agendamento.py      # Agendamento
│   ├── salao.py            # Salao (classe principal)
│   ├── corte_masculino.py  # CorteMasculino
│   ├── corte_feminino.py   # CorteFeminino
│   ├── barba.py            # Barba
│   ├── pintar_cabelo.py    # PintarCabelo
│   └── sobrancelha.py      # Sobrancelha
├── main.py                 # Demonstração do sistema
├── README.md
└── ESTRUTURA.md
```

## Classes do Sistema

### Pasta `model/`

#### Classes Principais
- **Service**: Classe base para todos os serviços do salão (com atributos privados)
- **ServiceFactory**: Padrão Factory para criação de serviços (arquivo separado)
- **PriceStrategy**: Interface abstrata para estratégias de preço
- **Cliente**: Representa um cliente com histórico de agendamentos
- **Profissional**: Representa um profissional que realiza serviços
- **Agendamento**: Conecta cliente, profissional e serviço com data/hora
- **Salao**: Classe principal que gerencia todo o sistema

#### Classes de Serviços Específicos
- **CorteMasculino**: Serviço de corte masculino (30min, R$25,00)
- **CorteFeminino**: Serviço de corte feminino (45min, R$40,00)
- **Barba**: Serviço de barba (20min, R$15,00)
- **PintarCabelo**: Serviço de pintura de cabelo (120min, R$80,00)
- **Sobrancelha**: Serviço de sobrancelha (15min, R$20,00)

### Arquivo principal
- **main.py**: Demonstração completa do funcionamento do sistema
  - Cadastro de clientes e profissionais
  - Criação de serviços (via Factory e classe direta)
  - Agendamentos com diferentes estratégias de preço
  - Histórico de clientes e relatórios

## Padrões de Projeto Implementados

### Factory Pattern (ServiceFactory)
- Centraliza a criação de objetos Service
- Facilita manutenção e extensibilidade
- Padroniza a criação de serviços

### Strategy Pattern (PriceStrategy)
- Permite alternar dinamicamente entre diferentes cálculos de preço
- Evita estruturas condicionais complexas
- Facilita adição de novas estratégias de preço

## Pilares da POO Aplicados

### Encapsulamento
- Atributos privados controlados por métodos
- Listas internas gerenciadas pelas próprias classes

### Herança
- PriceStrategy como classe base abstrata
- Subclasses implementam comportamentos específicos

### Polimorfismo
- Estratégias de preço usadas de forma genérica
- Mesmo método calcular() com comportamentos diferentes

### Abstração
- Classes representam conceitos do mundo real
- Interfaces claras e bem definidas