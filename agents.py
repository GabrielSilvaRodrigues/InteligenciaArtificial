# %% [markdown]
# # Motor do Jogo e Árbitro
# 
# Define o ambiente para o problema de busca adversarial que o jogo irá utilizar:
# - Define as regras e a dinâmica do jogo de retirar palitos
# - Fornece uma classe de controle (Referee) para simular uma partida entre dois agentes
# - É a base sobre a qual algoritmos de busca adversarial (minimax, α-β, etc.) podem ser testados

# %%
import random

# --- PART 1: THE GAME ENGINE (The Environment) ---


class GameState:
    def __init__(self, sticks, turn="MAX"):
        self.sticks = sticks
        self.turn = turn  # "MAX" (Agent) or "MIN" (Opponent)

    def get_actions(self):
        """Returns possible moves (cannot take more than are left)."""
        if self.sticks >= 3:
            return [1, 2, 3]
        if self.sticks == 2:
            return [1, 2]
        if self.sticks == 1:
            return [1]
        return []

    def generate_child(self, action):
        """Returns a new state after taking 'action' sticks."""
        next_turn = "MIN" if self.turn == "MAX" else "MAX"
        return GameState(self.sticks - action, next_turn)

    def is_terminal(self):
        return self.sticks <= 0

    def evaluate(self):
        """Terminal utility: If it's MAX's turn and 0 sticks are left, MAX lost."""
        if self.sticks <= 0:
            return -1 if self.turn == "MAX" else 1
        return 0

# %%
class Referee:
    def __init__(self, state, agent_max, agent_min):
        self.state = state
        self.agent_max = agent_max
        self.agent_min = agent_min

    def play(self):
        print(f"--- Game Start! Sticks: {self.state.sticks} ---")
        while not self.state.is_terminal():
            current_agent = (
                self.agent_max
                if self.state.turn == "MAX"
                else self.agent_min
            )
            move = current_agent.get_move(self.state)

            print(f"{self.state.turn} takes {move} sticks.")
            self.state = self.state.generate_child(move)
            print(f"Sticks remaining: {self.state.sticks} \n")

        winner = "MIN" if self.state.turn == "MAX" else "MAX"
        print(f"--- Game Over! Winner is {winner} ---")

# %% [markdown]
# ## Importar Agentes e Executar Jogo

# %%
import sys
sys.path.insert(0, '/workspaces/InteligenciaArtificial')

from game_engine import RandomAgent, AlphaBetaAgent

print("✓ Agentes importados com sucesso!")

# %% [markdown]
# ## Partida: AlphaBetaAgent vs RandomAgent

# %%
# Create agents
alpha_beta_agent = AlphaBetaAgent(depth=10)
random_agent = RandomAgent()

# Start fresh game
initial_state = GameState(sticks=15)
referee = Referee(initial_state, alpha_beta_agent, random_agent)

# Play!
referee.play()


