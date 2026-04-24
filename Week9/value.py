import numpy as np

size = 3
goal = (2, 2)
trap = (1, 1)
actions = ['U','D','L','R']

states = [(i,j) for i in range(size) for j in range(size)]

def move(s, a):
    i,j = s
    if a=='U': i-=1
    if a=='D': i+=1
    if a=='L': j-=1
    if a=='R': j+=1
    i = max(0, min(i, size-1))
    j = max(0, min(j, size-1))
    return (i,j)

def reward(s):
    if s == goal: return 0
    if s == trap: return -10
    return -1

def value_iteration():
    V = {s:0 for s in states}

    while True:
        delta = 0
        newV = V.copy()

        for s in states:
            if s in [goal, trap]: continue

            newV[s] = max([
                reward(move(s,a)) + 0.9 * V[move(s,a)]
                for a in actions
            ])

            delta = max(delta, abs(V[s]-newV[s]))

        V = newV
        if delta < 0.01: break

    return V

V = value_iteration()

print("Value Iteration Output:")
for s in states:
    print(s, ":", round(V[s],2))