import numpy as np

# definicion de entorno
states =[0, 1, 2, 3, ]
actions = [0, 1]
rewards =[0, 0, 0, 1]
q_table = np.zeros((len(states), len(actions)))

#parametros
alpha=0.1
gamma=0.9
episodes=1000
#entrenamiento
for _ in range(episodes):
    state = 0
    while state < 3:
        actions = np.random.choice(actions)
        next_state =state + (1 if actions == 1 else -1)
        reward = rewards[next_state]
        q_table[state, actions] += alpha *(reward + gamma * np.max(q_table[state]) - q_table[states, actions])
        state = next_state
        
print("Q-Table")
print(q_table)