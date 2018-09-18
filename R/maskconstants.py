import numpy as np
"""
Using constants instead of transposing / manually accessing memory in the massive matrix constantly
Unless its 3-4 elements, doing a series of checks is the fastest route to finding myself in a buggy mess
"""
BLACK = 0
WHITE = 1
DNC = 3
H1MASK = np.array([
      [DNC,BLACK,DNC],
      [BLACK,WHITE,BLACK],
      [DNC,BLACK,DNC]
          ])
H2MASK = [
      [DNC,BLACK,BLACK,DNC],
      [BLACK,WHITE,WHITE,BLACK],
      [DNC,BLACK,BLACK,DNC]
         ]
H3MASK = [
      [DNC,BLACK,DNC],
      [BLACK,WHITE,BLACK],
      [BLACK,WHITE,BLACK],
      [DNC,BLACK,DNC]
          ]
I1MASK = [
    [DNC, DNC, BLACK, BLACK, BLACK, DNC, DNC],
    [DNC, BLACK, BLACK, BLACK, BLACK, BLACK, DNC],
    [DNC, BLACK, BLACK, BLACK, BLACK, BLACK, DNC],
    [BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK],
    [DNC, BLACK, BLACK, BLACK, BLACK, BLACK, DNC],
    [DNC, BLACK, BLACK, BLACK, BLACK, BLACK, DNC],
    [DNC, DNC, BLACK, BLACK, BLACK, DNC, DNC]
]
I2MASK = [
    [DNC, DNC, BLACK, BLACK, BLACK, DNC, DNC],
    [DNC, BLACK, BLACK, BLACK, BLACK, BLACK, DNC],
    [DNC, BLACK, BLACK, BLACK, BLACK, BLACK, DNC],
    [BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK],
    [BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK],
    [DNC, BLACK, BLACK, BLACK, BLACK, BLACK, DNC],
    [DNC, BLACK, BLACK, BLACK, BLACK, BLACK, DNC],
    [DNC, DNC, BLACK, BLACK, BLACK, DNC, DNC]
]
I3MASK = [
   [DNC,DNC,BLACK,BLACK,BLACK,BLACK,DNC,DNC],
   [DNC,DNC,BLACK,BLACK,BLACK,BLACK,DNC,DNC],
   [DNC,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,DNC],
   [BLACK,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,BLACK],
   [DNC,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,DNC],
   [DNC,DNC,BLACK,BLACK,BLACK,BLACK,DNC,DNC],
   [DNC,DNC,BLACK,BLACK,BLACK,BLACK,DNC,DNC],
]
D1MASK = [
    [BLACK,BLACK,WHITE,BLACK,BLACK],
    [BLACK,BLACK,WHITE,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [DNC,BLACK,BLACK,BLACK,DNC]
]
D2MASK = [
    [BLACK,WHITE,WHITE,BLACK,BLACK],
    [BLACK,BLACK,WHITE,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [DNC,BLACK,BLACK,BLACK,DNC]
]
D3MASK = [
    [BLACK,BLACK,WHITE,WHITE,BLACK],
    [BLACK,BLACK,WHITE,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [DNC,BLACK,BLACK,BLACK,DNC]
]
D4MASK = [
    [BLACK,WHITE,WHITE,BLACK,BLACK],
    [BLACK,WHITE,WHITE,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [DNC,BLACK,BLACK,BLACK,DNC]
]
D5MASK = [
    [BLACK,BLACK,WHITE,WHITE,BLACK],
    [BLACK,BLACK,WHITE,WHITE,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [DNC,BLACK,BLACK,BLACK,DNC]
]
U1MASK = [
    [DNC,BLACK,BLACK,BLACK,DNC],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,WHITE,BLACK,BLACK],
    [BLACK,BLACK,WHITE,BLACK,BLACK]
]
U2MASK = [
    [DNC,BLACK,BLACK,BLACK,DNC],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,WHITE,BLACK,BLACK],
    [BLACK,BLACK,WHITE,WHITE,BLACK]
]
U3MASK = [
    [DNC,BLACK,BLACK,BLACK,DNC],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,WHITE,BLACK,BLACK],
    [BLACK,WHITE,WHITE,BLACK,BLACK]
]
U4MASK = [
    [DNC,BLACK,BLACK,BLACK,DNC],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,WHITE,WHITE,BLACK],
    [BLACK,BLACK,WHITE,WHITE,BLACK]
]
U5MASK = [
    [DNC,BLACK,BLACK,BLACK,DNC],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,BLACK,BLACK,BLACK,BLACK],
    [BLACK,WHITE,WHITE,BLACK,BLACK],
    [BLACK,WHITE,WHITE,BLACK,BLACK]
]
DU_MASKS = [D1MASK,D2MASK,D3MASK,D4MASK,D5MASK,U1MASK,U2MASK,U3MASK,U4MASK,U5MASK]
DU3_MASKS = [D1MASK,D2MASK,D3MASK,U1MASK,U2MASK,U3MASK]
