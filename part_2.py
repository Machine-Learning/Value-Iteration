import numpy as np
import sys
import os

MINM = -100000000

#Hyperparameters
DELTA = 0.001
GAMMA = 0.999

#Define all pos
all_pos=[]
all_pos.append('C')
all_pos.append('N')
all_pos.append('S')
all_pos.append('E')
all_pos.append('W')

#Define all state
all_states=[]
all_states.append('D')
all_states.append('R')

max_mat = 2
max_arrow = 3
E_left = 0
STEP_COST = -10
sc = 0

#Reward for each action
action_reward = {
    'UP': STEP_COST,
    'LEFT': STEP_COST,
    'DOWN': STEP_COST,
    'RIGHT': STEP_COST,
    'STAY': STEP_COST,
    'SHOOT': STEP_COST,
    'HIT': STEP_COST,
    'CRAFT': STEP_COST,
    'GATHER': STEP_COST,
    'NONE': STEP_COST
}

#Define rewards for all states
rewards = {}
for s in all_pos:
    rewards[s] = 0

#Dictionnary of possible actions. We have two "end" states (1,2 and 2,2)
actions = {
    'W':('RIGHT', 'STAY', 'SHOOT'), 
    'N':('DOWN', 'STAY', 'CRAFT'),
    'E':('LEFT', 'STAY', 'SHOOT', 'HIT'),
    'S':('UP', 'STAY', 'GATHER'),
    'C':('UP', 'DOWN', 'LEFT', 'RIGHT', 'STAY', 'SHOOT', 'HIT')
    }

#Dictionary for integer mapping of pos of IJ
pos_map = {
    'C' : 0,
    'N' : 1,
    'S' : 2,
    'E' : 3,
    'W' : 4
}

#Dictionary for integer mapping of states of MM
state_map = {
    'D' : 0,
    'R' : 1
}

#Dictionary for integer mapping of actions
action_map = {
    'UP': 0,
    'LEFT': 1,
    'DOWN': 2,
    'RIGHT': 3,
    'STAY': 4,
    'SHOOT': 5,
    'HIT': 6,
    'CRAFT': 7,
    'GATHER': 8,
    'NONE': 9
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

def prob(a,p,m,arr,s,h,p1,m1,arr1,s1,h1):
    p_MM = 0
    var = 0
    if s == 'D' and s1 == 'R':
        p_MM = 0.2
    elif s == 'D' and s1 == 'D':
        p_MM = 0.8
    elif s == 'R' and s1 == 'R':
        p_MM = 0.5
    elif s == 'R' and s1 == 'D':
        p_MM = 0.5
        var = 1
    
    if var == 1 and (p == 'C' or p == 'E'):
        if arr1!=0 or m!=m1:
            return 0
        elif (h+1)!=h1 and (h!=4 or h1!=4):
            return 0
        # (h+1)==h1 or (h==4 and h1==4)
        else:
            var = 2
    if a == 'UP':
        if m!=m1 or (var!=2 and arr!=arr1) or (var!=2 and h!=h1):
            return 0
        if p == 'S':
            if p1 == 'C':
                return probability[p]*p_MM
            elif p1 == fail[p]:
                return (1-probability[p])*p_MM
            else:
                return 0
        elif p == 'C':
            if var == 2:
                if p1 == p:
                    return p_MM
                else:
                    return 0
            if p1 == 'N':
                return probability[p]*p_MM
            elif p1 == fail[p]:
                return (1-probability[p])*p_MM
            else:
                return 0
        else:
            return 0
    elif a == 'DOWN':
        if m!=m1 or (var!=2 and arr!=arr1) or (var!=2 and h!=h1):
            return 0
        if p == 'N':
            if p1 == 'C':
                return probability[p]*p_MM
            elif p1 == fail[p]:
                return (1-probability[p])*p_MM
            else:
                return 0
        elif p == 'C':
            if var == 2:
                if p1 == p:
                    return p_MM
                else:
                    return 0
            if p1 == 'S':
                return probability[p]*p_MM
            elif p1 == fail[p]:
                return (1-probability[p])*p_MM
            else:
                return 0
        else:
            return 0
    elif a == 'LEFT':
        if m!=m1 or (var!=2 and arr!=arr1) or (var!=2 and h!=h1):
            return 0
        if p == 'E':
            if var == 2:
                if p1 == p:
                    return p_MM
                else:
                    return 0
            if (p1 == 'C' and E_left == 0) or (p1 == 'W' and E_left == 1):
                return probability[p]*p_MM
            elif p1 == fail[p]:
                return (1-probability[p])*p_MM
            else:
                return 0
        elif p == 'C':
            if var == 2:
                if p1 == p:
                    return p_MM
                else:
                    return 0
            if p1 == 'W':
                return probability[p]*p_MM
            elif p1 == fail[p]:
                return (1-probability[p])*p_MM
            else:
                return 0
        else:
            return 0
    elif a == 'RIGHT':
        if m!=m1 or (var!=2 and arr!=arr1) or (var!=2 and h!=h1):
            return 0
        if p == 'W':
            if p1 == 'C':
                return probability[p]*p_MM
            elif p1 == fail[p]:
                return (1-probability[p])*p_MM
            else:
                return 0
        elif p == 'C':
            if var == 2:
                if p1 == p:
                    return p_MM
                else:
                    return 0
            if p1 == 'E':
                return 1*p_MM
            else:
                return 0
        else:
            return 0
    elif a == 'STAY':
        if m!=m1 or (var!=2 and arr!=arr1) or (var!=2 and h!=h1):
            return 0
        if var == 2 and (p == 'C' or p == 'E'):
                if p1 == p:
                    return p_MM
                else:
                    return 0
        if p1 == p:
#             print('reached 1')
            return probability[p]*p_MM
        elif p1 == fail[p]:
#             print('reached 2')
            return (1-probability[p])*p_MM
        else:
            return 0
        
    elif a == 'SHOOT':
        if p!=p1 or m!=m1:
            return 0
        if var == 2 and (p == 'C' or p == 'E'):
            if p == 'C':
                return p_MM
            elif p == 'E':
                return p_MM
        if arr == arr1+1 and (p == 'C' or p == 'E' or p == 'W'):
            if p == 'C':
                if h == h1+1:
                    return 0.5*p_MM
                elif h == h1:
                    return 0.5*p_MM
                else:
                    return 0
            elif p == 'E':
                if h == h1+1:
                    return 0.9*p_MM
                elif h == h1:
                    return 0.1*p_MM
                else:
                    return 0
            elif p == 'W':
                if h == h1+1:
                    return 0.25*p_MM
                elif h == h1:
                    return 0.75*p_MM
                else:
                    return 0
        else:
            return 0
        
    elif a == 'HIT':
        if p!=p1 or m!=m1 or (var!=2 and arr!=arr1):
            return 0
        if var == 2 and (p == 'C' or p == 'E'):
            if p == 'C':
                return p_MM
            elif p == 'E':
                return p_MM
        if p == 'C':
            if h == h1+2 or (h == h1+1 and h1 == 0):
                return 0.1*p_MM
            elif h == h1:
                return 0.9*p_MM
            else:
                return 0
        elif p == 'E':
            if h == h1+2 or (h == h1+1 and h1 == 0):
                return 0.2*p_MM
            elif h == h1:
                return 0.8*p_MM
            else:
                return 0
        else:
            return 0
        
    elif a == 'CRAFT':
        if p!=p1 or h!=h1 or m==0:
            return 0
        if p == 'N' and m>=1 and m == m1+1:
            if arr == 0:
                if arr+1 == arr1:
                    return 0.5*p_MM
                elif arr+2 == arr1:
                    return 0.35*p_MM
                elif arr+3 == arr1:
                    return 0.15*p_MM
                else:
                    return 0
            elif arr == 1:
                if arr+1 == arr1:
                    return 0.5*p_MM
                elif arr+2 == arr1:
                    return 0.5*p_MM
                else:
                    return 0
            elif arr == 2:
                if arr+1 == arr1:
                    return p_MM
                else:
                    return 0
            elif arr == 3:
                if arr == arr1:
                    return p_MM
                else:
                    return 0
        else:
            return 0
        
    elif a == 'GATHER':
        if p!=p1 or h!=h1 or arr!=arr1:
            return 0
        if p == 'S':
            if m+1 == m1 and m<=1:
                return 0.75*p_MM
            elif m == m1 and m<=1:
                return 0.25*p_MM
            elif m == m1 and m==2:
                return p_MM
            else:
                return 0
        else:
            return 0
    
    elif a == 'NONE':
        return 0

def iterate():
    iteration = 0
    
    pos = 'W'
    mat = 0
    arrow = 0
    state = 'D'
    health = 4
    
    value = np.zeros((len(all_pos),max_mat+1,max_arrow+1,len(all_states),health+1))
    action = np.empty((len(all_pos),max_mat+1,max_arrow+1,len(all_states),health+1), dtype='<U7')
    
    while True:
#     while iteration <= 1:
        biggest_change = 0
        
        tmp = np.zeros((len(all_pos),max_mat+1,max_arrow+1,len(all_states),health+1))
        tmp[:] = MINM
        action[:] = 'NOTSET'
        
        for p in all_pos:
            for m in range(0,max_mat+1):
                for arr in range(0,max_arrow+1):
                    for s in all_states:
                        for h in range(0,health+1):

                            num_p = pos_map[p]
                            num_s = state_map[s]
                            
                            if h == 0:
                                action[num_p,m,arr,num_s,h] = 'NONE'
                                tmp[num_p,m,arr,num_s,h] = 0
                                continue
                                
                            # loop over actions
                            for a in actions[p]:
                                if a == 'SHOOT' and arr == 0:
                                    continue
                                elif a == 'CRAFT' and (m == 0):
                                    continue
#                                 elif a == 'GATHER' and m == 2:
#                                     continue
                                    
                                state_value = 0
                                var = 0
                                for p1 in all_pos:
                                    for m1 in range(0,max_mat+1):
                                        for arr1 in range(0,max_arrow+1):
                                            for s1 in all_states:
                                                for h1 in range(0,health+1):
                                                    
#                                                     reward = action_reward[a]
                                                    reward = STEP_COST
                                                    if sc == 1 and a == 'STAY':
                                                        reward = 0
                                                    if h1 == 0:
                                                        reward += 50
                                                    elif s == 'R' and s1 == 'D' and (p == 'E' or p == 'C') and ((h+1)==h1 or (h==4 and h1==4)) and arr1==0 and m==m1:
                                                        reward -= 40
                                                    num_p1 = pos_map[p1] 
                                                    num_s1 = state_map[s1]
#                                                     print(reward,round((reward + GAMMA*value[num_p1,m1,arr1,num_s1,h1])*prob(a,p,m,arr,s,h,p1,m1,arr1,s1,h1),8))
                                                    pr = prob(a,p,m,arr,s,h,p1,m1,arr1,s1,h1)
                                                    state_value += (reward + GAMMA*value[num_p1,m1,arr1,num_s1,h1])*pr
                                                    if pr > 1e-8:
                                                        var = 1
#                                                         print('\tAction = ',a,', Initial = ',p,m,arr,s,h,', Final = ',p1,m1,arr1,s1,h1,', Value = ',round((reward + GAMMA*value[num_p1,m1,arr1,num_s1,h1])*prob(a,p,m,arr,s,h,p1,m1,arr1,s1,h1),8))
                                if var == 0:
                                    state_value = MINM
#                                 print('\tAction = ',a,', Initial = ',p,m,arr,s,h,', Value = ',state_value,', Temp value = ',tmp[num_p,m,arr,num_s,h])
#                                 taking max of all the values
                                if state_value >= tmp[num_p,m,arr,num_s,h]:
                                    action[num_p,m,arr,num_s,h] = a
#                                     print('\tMin action = ',a)
                                    tmp[num_p,m,arr,num_s,h] = state_value
                                
                            biggest_change = max(biggest_change,abs(tmp[num_p,m,arr,num_s,h]-value[num_p,m,arr,num_s,h]))
                            
        np.copyto(value,tmp)
                
        print("iteration=%d"%iteration)
        for p in all_pos:
            for m in range(0,max_mat+1):
                for arr in range(0,max_arrow+1):
                    for s in all_states:
                        for h in range(0,health+1):
                                print(end="(")
                                print(p,end=",")
                                print(m,end=",")
                                print(arr,end=",")
                                print(s,end=",")
                                print(h*25,end="):")
                                num_p = pos_map[p]
                                num_s = state_map[s]
                                print(action[num_p,m,arr,num_s,h],end="=[")
                                print("{0:.3f}".format(value[num_p,m,arr,num_s,h]),end="]\n")

       #See if the loop should stop now         
        if biggest_change < DELTA:
            break
        iteration += 1

initial = sys.stdout
if not os.path.exists('outputs'):
    os.makedirs('outputs')

# task 1        
sys.stdout = open('./outputs/part_2_trace.txt', 'w')
iterate()
sys.stdout = initial

# task 2, case 1
E_left = 1
sys.stdout = open('./outputs/part_2_task_2.1_trace.txt', 'w')
iterate()
sys.stdout = initial
E_left = 0

# task 2, case 2
sc = 1
sys.stdout = open('./outputs/part_2_task_2.2_trace.txt', 'w')
iterate()
sys.stdout = initial
sc = 0

# task 2, case 3
GAMMA = 0.25
sys.stdout = open('./outputs/part_2_task_2.3_trace.txt', 'w')
iterate()
sys.stdout = initial
GAMMA = 0.999