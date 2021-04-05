from enum import Enum
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s',level=logging.DEBUG)

class Pos(Enum):
    W = 'W'
    N = 'N'
    E = 'E'
    S = 'S'
    C = 'C'
    
class Mat(Enum):
    v0 = 0
    v1 = 1
    v2 = 2

class Arrow(Enum):
    v0 = 0
    v1 = 1
    v2 = 2
    v3 = 3
    
class State(Enum):
    D = 'D'
    R = 'R'
    
class Action(Enum):
    UP = 'UP'
    LEFT = 'LEFT'
    DOWN = 'DOWN'
    RIGHT = 'RIGHT'
    STAY = 'STAY'
    SHOOT = 'SHOOT'
    HIT = 'HIT'
    CRAFT =  'CRAFT'
    GATHER = 'GATHER'
    NONE = 'NONE'
    
pos = Pos('C')
# Discount Factor
GAMMA = 0.999
# Convergence or Bellman error
DELTA = 1e-3
STEP_COST = -10

print(pos)
if pos == Pos('C'):
    print('C')
try:
    pos = Pos('R')
except ValueError as e:
    print("invalid Size (", e.args[0].split()[0],
          "). Size must be one of 'small', 'medium' or 'big'", sep='')

logging.debug("(<pos>,<mat>,<arrow>,<state>,<health>):<action>=[<state_value>]")