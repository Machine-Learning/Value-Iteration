Assignment #2
Part #2
Team # 70

Members : 
    Prince Singh Tomar (2019101021)
    Utkarsh Upadhyay (2019101010)

    --------------------------------------------------------------------------------------------------------------------------------------
Task # 1 :

Convergence : 118
In West Square :
    - If The Mighty Monster is in dormant state and if Indiana Jones has got arrows(>0) then Indiana Jones chooses to `SHOOT` only if The Mighty Monster has less health, else Indiana Jones moves `RIGHT` to attack The Mighty Monster with `HIT` before The Mighty Monster gets back to the attack state.
    - If The Mighty Monster is in attack state, Indiana Jones tries to stay out of Mighty Monster’s attack range given Indiana Jones has arrows and Mighty Monster’s health is less, else Indiana Jones moves `RIGHT` to `HIT`,`CRAFT` or `GATHER`, depending on how much materials Indiana Jones has and Mighty Monster’s health. Depending on his arrows and Mighty Monster’s health, Indiana Jones chooses to `SHOOT` or `STAY`.
In North Square :
    - If The Mighty Monster is in dormant state, Indiana Jones moves `DOWN` if Indiana Jones has no materials and if Indiana Jones has got arrows, or if Mighty Monster’s health is 100/4 and Indiana Jones has only one arrow. In all other cases Indiana Jones chooses to `CRAFT` arrows.
    -If The Mighty Monster is in attack state, Indiana Jones tries to `STAY` out of Mighty Monster’s attack range. Indiana Jones chooses to stay If Indiana Jones has no material or If Indiana Jones has 3 arrows. Otherwise Indiana Jones chooses to `CRAFT`. Indian Jones chooses to move `DOWN` to `GATHER` materials If Mighty Monster’s health is totaly full, and if Indiana Jones does not have arrows or materials. Also, if Indiana Jones has got arrows and Mighty Monster’s health reaches 100/4, Indiana Jones chooses to `STAY` .
In East Square :
    - If The Mighty Monster is in dormant state, Indiana Jones always attacks. Indiana Jones attacks with `HIT`, if Indiana Jones is out of arrows or If The Mighty Monster has full health and Indiana Jones does not have all his arrows. Otherwise, Indiana Jones attacks by `SHOOT`.
    - If The Mighty Monster is in attack state, Indiana Jones still attacks. Indiana Jones attacks with `HIT`, if Indiana Jones is out of arrows, or If The Mighty Monster has totaly full health, else Indiana Jones attacks by `SHOOT`.
In South Square :
    - If The Mighty Monster is in dormant state,  Indiana Jones chooses to `GATHER` only if Indiana Jones does not have arrows and materials, and if Mighty Monster’s health is 100/4. In all other case, Indiana Jones moves `UP` to attack or `CRAFT`.
    - If The Mighty Monster is in attack state, Indiana Jones moves `UP` if Mighty Monster’s health is 100/1 and Indiana Jones has got insufficient arrows, or if Indiana Jones has 2 materials and has got insufficient arrows. Indiana Jones either chooses to `GATHER` materials or `STAY` depending on how many materials and arrows are on Indiana Jones.
In center Square :
    - If The Mighty Monster is in dormant state, Indiana Jones moves `RIGHT` to attack if Indiana Jones has no materials, and moves `UP` to craft or again `RIGHT` to attack depending on, how many arrows Indiana Jones has, and Mighty Monster’s health.
    - If The Mighty Monster is in attack state, Indiana Jones tries to stay out of Mighty Monster’s attack range by going `UP` or `DOWN`. If Indiana Jones has got arrows, Indiana Jones moves `LEFT` to attack The Mighty Monster by shooting. If  Indiana Jones has arrows and Mighty Monster’s health is 100/4, Indiana Jones attacks The Mighty Monster by `SHOOT`.

End States : 
1)  Initial State: (W,0,0,D,100)
    Action Taken: RIGHT     ;  Resulting State: (C,0,0,D,100)
    Action Taken: RIGHT     ;  Resulting State: (E,0,0,D,100)
    Action Taken: Hit       ;  Resulting State: (E,0,0,D,50)
    Action Taken: Hit       ;  Resulting State: (E,0,0,D,0)
    End State: (E,0,0,D,0)
    End state if Mighty Monster reaches Zero health.

2)  Initial State: (C,2,0,R,100)
    Action Taken: Up        ;  Resulting State: (N,2,0,R,100)
    Action Taken: Craft     ;  Resulting State: (N,1,1,R,100)
    Action Taken: Craft     ;  Resulting State: (N,0,2,R,100)
    Action Taken: Stay      ;  Resulting State: (N,0,2,R,100)
    Here Indiana Jones Will prefer to avoid Mighty Monster. He will again start attacking and roaming if Mighty Monster moves to Dormant state. There is another possibility that the failure of stay action and therefore leading of Indiana Jones to East block and exposing it to the Mighty Monster. Since Former option is more probable hence it's actions will be:
    Action Taken: Stay(Fail);  Resulting State: (N,0,2,D,100)
    Action Taken: Down      ;  Resulting State: (C,0,2,D,100)
    Action Taken: RIGHT     ;  Resulting State: (E,0,2,D,100)
    Action Taken: Hit       ;  Resulting State: (E,0,2,D,50)
    Action Taken: Shoot     ;  Resulting State: (E,0,2,D,25)
    Action Taken: Shoot     ;  Resulting State: (E,0,2,D,0)
    End State: (E,0,2,D,0)
    End state again reaches only if Mighty Monster's health reaches Zero.

    --------------------------------------------------------------------------------------------------------------------------------------
Task # 2:

    Case 1: In this case, not much change is observed in our policy. This is because Indiana Jones in Task 1 policy tried to avoid CENTER pos, as it makes him vulnerable to attack from Mighty Monster. Similar pattern is observed here as well.
    The number of iterations in this case remain almost same (120).
    
    Case 2: In this case, STAY action seems to become a better choice for Indiana Jones in the WEST pos.
    The number of iterations required for convergence here are again similar (57).

    Case 3: Due to lower value of GAMMA, future rewards become less valuable, and as a result, the convergence occurs in much less iterations (8)!.


