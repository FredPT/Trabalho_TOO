#  Sistema para Gerenciamento de Salão de Beleza  
**Tecnologia Orientada a Objetos — Avaliação Prática Final**

---

##  Diagrama de Classes UML

![Diagrama](./Diagrama/Diagrama_Salão.png)

---

##  Descrição do Sistema

Sistema completo para gerenciamento de salão de beleza implementado em Python, aplicando todos os pilares da POO e padrões de projeto **Factory** e **Strategy**.

### **Funcionalidades**
- Cadastro de clientes e profissionais
- Gerenciamento de serviços (cortes, barba, sobrancelha e pintura)
- Sistema de agendamentos com validações
- Cálculo dinâmico de preços com diferentes estratégias
- Histórico completo de atendimentos
- Validação de competências dos profissionais

---

##  Como Usar o Sistema

### **1. Criar o Salão**
```python
from model.salao import Salao
salao = Salao()
```

### **2. Cadastrar Clientes**
```python
cliente = salao.cadastrarCliente("Frederico", "51999999999")
```

### **3. Cadastrar Profissionais**
```python
profissional = salao.cadastrarProfissional("Carmem", "Cabeleireira")
```

### **4. Adicionar Serviços aos Profissionais**
```python
from model.servicefactory import ServiceFactory
servico_corte = ServiceFactory.criarServico("CorteM")
profissional.adicionarServico(servico_corte)
```

### **5. Fazer Agendamentos**
```python
from datetime import datetime
from model.preco_promocional import PrecoPromocional

dataHora = datetime(2025, 12, 15, 14, 30)
agendamento = salao.agendar(dataHora, cliente, profissional, "CorteM", PrecoPromocional())
```

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
| PrecoPromocional | 20%      | Promoções especiais |
| PrecoFidelidade  | 10%      | Clientes frequentes |

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