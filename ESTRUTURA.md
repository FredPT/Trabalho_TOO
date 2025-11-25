# Estrutura do Sistema de Gerenciamento de Salão de Beleza

## Estrutura de Arquivos

```
Trabalho_Final/
├── model/
│   ├── __init__.py
│   ├── service.py      # Service, ServiceFactory, PriceStrategy
│   ├── cliente.py      # Cliente
│   ├── profissional.py # Profissional
│   ├── agendamento.py  # Agendamento
│   └── salao.py        # Salao (classe principal)
├── main.py             # Demonstração do sistema
├── README.md
└── ESTRUTURA.md
```

## Classes do Sistema

### Pasta `model/`
- **Service**: Representa um serviço do salão
- **ServiceFactory**: Padrão Factory para criação de serviços
- **PriceStrategy**: Interface abstrata para estratégias de preço
- **Cliente**: Representa um cliente com histórico
- **Profissional**: Representa um profissional que realiza serviços
- **Agendamento**: Conecta cliente, profissional e serviço
- **Salao**: Classe principal que gerencia todo o sistema

### Arquivo principal
- **main.py**: Demonstração do funcionamento do sistema

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