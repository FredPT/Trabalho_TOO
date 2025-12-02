#  Sistema para Gerenciamento de Salão de Beleza  
**Tecnologia Orientada a Objetos — Avaliação Prática Final**

---

##  Diagrama de Classes UML

![Diagrama](./Diagrama/Diagrama_Salão.png)

---

##  Descrição do Sistema

Sistema completo para gerenciamento de salão de beleza implementado em Python, aplicando todos os pilares da **POO**.

### **Objetivos**
- Implementar todos os **4 pilares da POO** (Abstração, Encapsulamento, Herança e Polimorfismo)
- Aplicar padrões **Factory** e **Strategy**
- Criar sistema funcional com validações
- Demonstrar boas práticas de programação

### **Funcionalidades**
- Cadastro de clientes e profissionais
- Gerenciamento de serviços com diferentes preços
- Sistema de agendamentos com validações
- Cálculo dinâmico de preços com diferentes estratégias
- Histórico completo de atendimentos
- Validação de competências dos profissionais

---

##  Serviços Disponíveis

| Código      | Serviço         | Duração | Preço Base |
|-------------|-----------------|---------|------------|
| CorteM      | Corte Masculino | 30 min  | R$ 25,00   |
| CorteF      | Corte Feminino  | 45 min  | R$ 40,00   |
| Barba       | Barba           | 15 min  | R$ 15,00   |
| Pintar      | Pintar Cabelo   | 120 min | R$ 80,00   |
| Sobrancelha | Sobrancelha     | 15 min  | R$ 20,00   |

---

##  Estratégias de Preço

| Estratégia       | Desconto | Uso                 |
|------------------|----------|---------------------|
| PrecoNormal      | 0%       | Preço padrão        |
| PrecoFidelidade  | 10%      | Clientes frequentes |
| PrecoPromocional | 20%      | Promoções especiais |

---

#  Arquitetura do Sistema

##  Estrutura de Arquivos
```
Trabalho_TOO/
├── model/
│    ├── salao.py              # Classe principal do sistema
│    ├── cliente.py            # Gerenciamento de clientes
│    ├── profissional.py       # Gerenciamento de profissionais
│    ├── agendamento.py        # Lógica de agendamentos
│    ├── service.py            # Classe base de serviços
│    ├── servicefactory.py     # Factory para criação de serviços
│    ├── price_strategy.py     # Interface de estratégias de preço
│    ├── preco_normal.py       # Estratégia preço normal
│    ├── preco_promocional.py  # Estratégia preço promocional
│    ├── preco_fidelidade.py   # Estratégia preço fidelidade
│    ├── corte_masculino.py    # Serviço corte masculino
│    ├── corte_feminino.py     # Serviço corte feminino
│    ├── barba.py              # Serviço barba
│    ├── pintar_cabelo.py      # Serviço pintura de cabelo
│    └── sobrancelha.py        # Serviço sobrancelha
├── main.py                    # Demonstração do sistema
└── README.md
```

---

##  Pilares da POO Aplicados

### **Abstração**
- Classes modelam entidades do mundo real (Cliente, Profissional, Agendamento)
- Interfaces abstratas (PriceStrategy) definem contratos claros

### **Encapsulamento**
- Atributos privados com getters/setters
- Controle de acesso aos dados internos
- Validações nos métodos de modificação

### **Herança**
- Serviços específicos herdam de Service
- Estratégias de preço herdam de PriceStrategy

### **Polimorfismo**
- Diferentes estratégias de preço com mesmo método
- ServiceFactory cria diferentes tipos de serviço

---

##  Descrição Detalhada das Classes

### **Classes Principais**

#### **Salao**
- **Responsabilidade:** Gerenciar todo o sistema do salão
- **Pilares POO:** Encapsulamento (listas privadas), Abstração (interface simples)
- **Funcionalidades:**
  - Cadastro de clientes e profissionais
  - Criação de agendamentos com validações
  - Controle de listas internas

#### **Cliente**
- **Responsabilidade:** Representar clientes do salão
- **Pilares POO:** Encapsulamento (atributos privados com getters/setters)
- **Funcionalidades:**
  - Armazenar dados pessoais (nome, telefone)
  - Manter histórico de agendamentos
  - Validação automática de dados (strip)

#### **Profissional**
- **Responsabilidade:** Representar profissionais do salão
- **Pilares POO:** Encapsulamento, Abstração (interface para verificar competências)
- **Funcionalidades:**
  - Gerenciar especialidade e serviços oferecidos
  - Validar se pode realizar determinado serviço
  - Controlar lista de serviços habilitados

#### **Agendamento**
- **Responsabilidade:** Conectar cliente, profissional e serviço
- **Pilares POO:** Encapsulamento, Polimorfismo (uso de estratégias)
- **Funcionalidades:**
  - Armazenar data/hora com validação
  - Calcular valor final usando estratégias
  - Manter referências para todas as entidades

---

### **Hierarquia de Serviços**

#### **Service** - *Classe Base Abstrata*
- **Responsabilidade:** Definir estrutura comum para todos os serviços
- **Pilares POO:** Abstração, Encapsulamento
- **Atributos:** nome, duração, preço (todos privados com validações)

#### **Classes Filhas de Service:**
- **CorteMasculino:** Herda de Service (30 min, R$ 25,00)
- **CorteFeminino:** Herda de Service (45 min, R$ 40,00)
- **Barba:** Herda de Service (15 min, R$ 15,00)
- **PintarCabelo:** Herda de Service (120 min, R$ 80,00)
- **Sobrancelha:** Herda de Service (15 min, R$ 20,00)

**Pilar Aplicado:** **Herança** - Todas herdam estrutura e comportamento da classe Service

---

### **Padrão Factory**

#### **ServiceFactory**
- **Responsabilidade:** Criar instâncias de serviços dinamicamente
- **Padrão:** Factory Method
- **Funcionalidade:** Método estático criarServico() que retorna objetos específicos baseado em string
- **Vantagem:** Desacopla criação de objetos do código cliente

### **Padrão Strategy**

#### **PriceStrategy** - *Interface Abstrata*
- **Responsabilidade:** Definir contrato para estratégias de preço
- **Padrão:** Strategy Pattern
- **Método Abstrato:** calcular(preco_base)

#### **Estratégias Concretas:**
- **PrecoNormal:** Retorna preço base sem alteração (0% desconto)
- **PrecoPromocional:** Aplica 20% de desconto (retorna preco_base * 0.8)
- **PrecoFidelidade:** Aplica 10% de desconto (retorna preco_base * 0.9)

**Pilar Aplicado:** **Polimorfismo** - Diferentes implementações do método calcular() com mesmo comportamento esperado

---

##  Validações do Sistema

- **Profissional:** Deve poder realizar o serviço solicitado
- **Data/Hora:** Deve ser objeto datetime válido
- **Preços:** Devem ser valores positivos
- **Duração:** Entre 1 e 499 minutos
- **Dados:** Strings são automaticamente limpos (strip)

---

##  Exemplo Completo de Uso

```python
from datetime import datetime
from model.salao import Salao
from model.servicefactory import ServiceFactory
from model.preco_promocional import PrecoPromocional

# Criar salão
salao = Salao()

# Cadastrar cliente
cliente = salao.cadastrarCliente("João", "51987654321")

# Cadastrar profissional
profissional = salao.cadastrarProfissional("Frederico", "Barbeiro")

# Adicionar serviços ao profissional
servico_corte = ServiceFactory.criarServico("CorteM")
servico_barba = ServiceFactory.criarServico("Barba")
profissional.adicionarServico(servico_corte)
profissional.adicionarServico(servico_barba)

# Fazer agendamento
dataHora = datetime(2025, 12, 20, 15, 0)
agendamento = salao.agendar(
    dataHora, 
    cliente, 
    profissional, 
    "CorteM", 
    PrecoPromocional()
)

print(agendamento.exibir_dados())
# Saída: Valor final com 20% de desconto
```  