import numpy as np

#Hyperparameters
DELTA = 0.001
GAMMA = 0.999         
NOISE = 0  

#Define all pos
all_pos=[]
all_pos.append('W')
all_pos.append('N')
all_pos.append('E')
all_pos.append('S')
all_pos.append('C')

#Define all state
all_states=[]
all_states.append('D')
all_states.append('R')

#Define rewards for all states
rewards = {}
for s in all_pos:
    rewards[s] = 0

#Dictionnary of possible actions. We have two "end" states (1,2 and 2,2)
actions = {
    'W':('RIGHT', 'STAY', 'SHOOT', 'NONE'), 
    'N':('DOWN', 'STAY', 'CRAFT', 'NONE'),
    'E':('LEFT', 'STAY', 'SHOOT', 'HIT', 'NONE'),
    'S':('UP', 'STAY', 'GATHER', 'NONE'),
    'C':('UP', 'DOWN', 'LEFT', 'RIGHT', 'STAY', 'SHOOT', 'HIT', 'NONE')
    }

#Define an initial policy
policy={}
for s in actions.keys():
    policy[s] = np.random.choice(actions[s])
print(policy)

#Define success probabilities for states
probability = {}
for s in all_pos:
    if s == 'E' or s == 'W':
        probability[s] = 1
    else:
        probability[s] = 0.85
print(probability)
        
#Define fail action for states
fail = {}
for s in all_pos:
    if s == 'E' or s == 'W':
        fail[s] = s
    else:
        fail[s] = 'E'
print(fail)

#Define initial value function 
V={}
for s in all_pos:
    if s in actions.keys():
        V[s] = 0
#     if s ==(2,2):
#         V[s]=-1
#     if s == (1,2):
#         V[s]=-1
#     if s == (2,3):
#         V[s]=1
print(V)

def iterate():
    iteration = 0
#     pos = 'W'
    pos = 0 # map 0->W, 1->N, 2->E, 3->S, 4->C
    mat = 0
    arrow = 0
    state = 0 # map 0->'D', 1->'R'
    health = 4
    while True:
        biggest_change = 0
        print("iteration=",iteration)
        for p in all_pos:
            for m in range(0,mat):
                for a in range(0,arrow):
                    for s in all_states:
                        for h in range(0,health):
                            
#                             print("State: ",p,"  Value: ", V[s])           
#                             if p in policy:
                            old_v = V[p]
                            new_v = 0

                            # loop over actions
                            for a in actions[posn]:
                                if a == 'UP':
                                    if p == 'S':
                                        nxt = 'C'
                                    else:
                                        nxt = 'N'
                                elif a == 'DOWN':
                                    if p == 'N':
                                        nxt = 'C'
                                    else:
                                        nxt = 'S'
                                elif a == 'LEFT':
                                    if p == 'E':
                                        nxt = 'C'
                                    else:
                                        nxt = 'W'
                                elif a == 'RIGHT':
                                    if p == 'W':
                                        nxt = 'C'
                                    else:
                                        nxt = 'E'
                                elif a == 'STAY':
                                    nxt = p
                                else:
                                    nxt = p

                #                 if a == 'SHOOT':
                #                     nxt = [s[0]-1, s[1]]
                #                 if a == 'HIT':
                #                     nxt = [s[0]-1, s[1]]
                #                 if a == 'CRAFT':
                #                     nxt = [s[0]-1, s[1]]
                #                 if a == 'GATHER':
                #                     nxt = [s[0]-1, s[1]]
                #                 if a == 'NONE':
                #                     nxt = [s[0]-1, s[1]]

                                #Choose a new random action to do (transition probability)
                                nxt_2 = fail[p]
                #                 print(probability[s])
                                print(nxt)
                                print(V[nxt])
                                print(V[nxt_2])
                                sigma = probability[s]*V[nxt] + (1-probability[s])*V[nxt_2]

                                #Calculate the value
                                v = rewards[p] + (GAMMA * sigma) 
                                if v > new_v: #Is this the best action so far? If so, keep it
                                    new_v = v
                                    policy[s] = a
                                print("(",p,end=",")
                                print(m,end=",")
                                print(a,end=",")
                                print(s,end=",")
                                print(h,end="):")
                                print(a,end=",[")
                                print(V[p],end="]")
           #Save the best of all actions for the state                                 
                V[p] = new_v
                biggest_change = max(biggest_change, np.abs(old_v - V[p]))

       #See if the loop should stop now         
        if biggest_change < DELTA:
            break
        iteration += 1

    for s in all_pos: 
        print("State: ",s,"  Value: ", V[s])
        
iterate()