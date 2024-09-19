import numpy as np

# Definición del entorno
states = [0, 1, 2, 3]
actions = [0, 1]  # 0: izquierda, 1: derecha
rewards = [0, 0, 0, 1]  # Recompensa en el estado 3
q_table = np.zeros((len(states), len(actions)))

# Parámetros
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
episodes = 1000

# Entrenamiento
for _ in range(episodes):
    state = 0  # Iniciar en el estado 0
    while state < 3:
        action = np.random.choice(actions)  # Elegir acción aleatoria
        next_state = state + (1 if action == 1 else -1)  # Moverse
        reward = rewards[next_state]
        
        # Actualizar Q-Table
        q_table[state, action] += alpha * (reward + gamma * np.max(q_table[next_state]) - q_table[state, action])
        
        state = next_state

print("Q-Table:")
print(q_table)
