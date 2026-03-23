# Inteligência Artificial - Jogo Adversarial com Minimax

Implementação de algoritmos de busca adversarial para um jogo de retirar palitos, demonstrando uso de técnicas clássicas de inteligência artificial como **Minimax** e **poda Alpha-Beta**.

## 📋 Descrição do Projeto

Este projeto implementa um ambiente de jogo adversarial onde dois agentes de IA competem em um jogo baseado em regras simples:
- **Jogo**: Retirar entre 1 a 3 palitos de uma pilha (iniciando com 15)
- **Objetivo**: Forçar o oponente a retirar o último palito (quem pega o último palito perde)
- **Agentes**:
  - **RandomAgent**: Escolhe movimentos aleatoriamente
  - **AlphaBetaAgent**: Usa algoritmo Minimax com poda Alpha-Beta para encontrar o melhor movimento

## 🏗️ Estrutura do Projeto

```
InteligenciaArtificial/
├── game_engine.py          # Motor do jogo, agentes e árbitro
├── minimax_agent.ipynb     # Notebook Jupyter com exemplos de execução
├── README.md               # Este arquivo
└── LICENSE                 # Licença do projeto
```

### Arquivos principais

#### `game_engine.py`
Contém:
- **RandomAgent**: Agente que executa movimentos aleatórios
- **AlphaBetaAgent**: Agente que implementa o algoritmo Minimax com poda Alpha-Beta
  - Parâmetro configurável `depth` para limitar a profundidade de busca
  - Implementação recursiva com otimização de poda

#### `minimax_agent.ipynb`
Notebook Jupyter com:
- Definição da classe `GameState` (representa o estado do jogo)
- Definição da classe `Referee` (árbitro que controla as partidas)
- Exemplos de partidas entre os agentes

## 🎮 Como Funciona

### GameState
Representa um estado do jogo com:
- **sticks**: Número de palitos restantes
- **turn**: Cujo turno é ("MAX" para o agente, "MIN" para o adversário)
- **get_actions()**: Retorna movimentos legais (1-3 palitos)
- **generate_child()**: Cria novo estado após um movimento
- **evaluate()**: Função de utilidade terminal (1 = MAX vence, -1 = MAX perde)

### AlphaBetaAgent
Implementa o algoritmo Minimax com poda Alpha-Beta:
```
alphabeta(estado, profundidade, alpha, beta, is_max)
  ├─ Caso base: profundidade = 0 ou estado terminal
  │  └─ Retorna avaliação do estado
  ├─ Se é turno de MAX:
  │  └─ Maximiza valor, atualiza alpha, faz poda se beta ≤ alpha
  └─ Se é turno de MIN:
     └─ Minimiza valor, atualiza beta, faz poda se beta ≤ alpha
```

## 🚀 Como Usar

### Executar uma partida via terminal
```bash
python3 /workspaces/InteligenciaArtificial/game_engine.py
```

### Executar um jogo com script Python
```bash
cd /workspaces/InteligenciaArtificial
python3 << 'EOF'
from game_engine import RandomAgent, AlphaBetaAgent

# [Incluir código do GameState e Referee aqui]

referee = Referee(GameState(15), AlphaBetaAgent(10), RandomAgent())
referee.play()
EOF
```

### Usar o Notebook Jupyter
```bash
jupyter notebook minimax_agent.ipynb
```

## 📊 Exemplos de Saída

```
--- Game Start! Sticks: 15 ---

MAX takes 3 sticks.
Sticks remaining: 12

MIN takes 3 sticks.
Sticks remaining: 9

MAX takes 1 sticks.
Sticks remaining: 8

MIN takes 2 sticks.
Sticks remaining: 6

MAX takes 2 sticks.
Sticks remaining: 4

MIN takes 1 sticks.
Sticks remaining: 3

MAX takes 3 sticks.
Sticks remaining: 0

--- Game Over! Winner is MAX ---
```

## 🔑 Conceitos Chave

- **Minimax**: Algoritmo de busca que avalia recursivamente todos os movimentos possíveis
- **Poda Alpha-Beta**: Otimização que reduz o número de nós avaliados eliminando branches que não afetam o resultado
- **Busca Adversarial**: Estratégia para jogos com dois jogadores com objetivos opostos
- **Função de Avaliação**: Métrica que determina a qualidade de um estado do jogo

## 🛠️ Tecnologias

- **Python 3.10+**
- **Jupyter Notebook** (opcional, para execução interativa)

## 📝 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

## 👤 Autor

Desenvolvido como parte da disciplina de Inteligência Artificial.
