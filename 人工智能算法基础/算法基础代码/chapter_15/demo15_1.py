
import gym
import numpy as np
import random
env = gym.make('FrozenLake-v0')

'''
While we choose the Action to take, we follow the epsilon-greedy policy: we either explore for new actions with a
probability epsilon or take an action which has a maximum value with a probability 1-epsilon. While updating the Q value, 
we simply select the action that has a maximum value + noise
'''

def epsilon_greedy_policy(state, epsilon, i):
    if random.uniform(0,1) < epsilon:
        return env.action_space.sample()
    else:
        return np.argmax(Q[state,:] + np.random.randn(1,env.action_space.n)*epsilon)
        
Q = np.zeros([env.observation_space.n, env.action_space.n])

# Definitiion of learning hyperparameters
ALPHA = 0.1
GAMMA = 0.999
NUMBER_EPISODES = 3000
epsilon = 0.015


total_REWARDS = []
for i in range(NUMBER_EPISODES):
    #Reset environment. Get first state.
    state = env.reset()
    sum_reward = 0
    done = False
    j = 0
    #The Q-Table learning algorithm
    while True:

        action = epsilon_greedy_policy(state, epsilon, i)
        #Get new state and reward from environment
        state_next, reward, done, _ = env.step(action)
        #Q table UPDATE
        Q[state,action] = Q[state,action] + ALPHA * (reward + GAMMA * np.max(Q[state_next,:]) - Q[state,action])
        
        sum_reward += reward
        state = state_next
        if done == True:
            break

    
    total_REWARDS.append(sum_reward)


print ("--- Q[S,A]-Table ---")
print (Q)
