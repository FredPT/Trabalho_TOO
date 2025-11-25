# Estrutura do Sistema de Gerenciamento de Salão de Beleza

## Arquivos do Sistema

### `service.py`
- **Service**: Classe que representa um serviço do salão
- **ServiceFactory**: Padrão Factory para criação de serviços
- **PriceStrategy**: Interface abstrata para estratégias de preço
- **PrecoNormal, PrecoPromocional, PrecoFidelidade**: Implementações concretas das estratégias

### `cliente.py`
- **Cliente**: Representa um cliente com histórico de agendamentos

### `profissional.py`
- **Profissional**: Representa um profissional que pode realizar serviços específicos

### `agendamento.py`
- **Agendamento**: Conecta cliente, profissional e serviço com cálculo de valor

### `salao.py`
- **Salao**: Classe principal que gerencia todo o sistema

### `main.py`
- Demonstração do funcionamento do sistema com exemplos práticos

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