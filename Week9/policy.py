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

def policy_iteration():
    policy = {s:np.random.choice(actions) for s in states if s not in [goal,trap]}
    V = {s:0 for s in states}

    while True:
        # Policy Evaluation
        for _ in range(20):
            for s in states:
                if s in [goal,trap]: continue
                a = policy[s]
                V[s] = reward(move(s,a)) + 0.9 * V[move(s,a)]

        # Policy Improvement
        stable = True
        for s in policy:
            old = policy[s]

            policy[s] = max(actions,
                key=lambda a: reward(move(s,a)) + 0.9 * V[move(s,a)]
            )

            if old != policy[s]:
                stable = False

        if stable: break

    return policy, V

policy, Vp = policy_iteration()

print("\nPolicy Iteration Output:")
for s in policy:
    print(s, "->", policy[s], "|", round(Vp[s],2))
