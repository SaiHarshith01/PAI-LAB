import math
b=[" "]*9
def show():
    for i in range(0,9,3): print(b[i],"|",b[i+1],"|",b[i+2])
    print()
def win(p):
    w=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[i]==b[j]==b[k]==p for i,j,k in w)
def minimax(m):
    if win("O"): return 1
    if win("X"): return -1
    if " " not in b: return 0
    best=-math.inf if m else math.inf
    for i in range(9):
        if b[i]==" ":
            b[i]="O" if m else "X"
            s=minimax(not m)
            b[i]=" "
            best=max(best,s) if m else min(best,s)
    return best
def move():
    worst,idx=math.inf,-1
    for i in range(9):
        if b[i]==" ":
            b[i]="O"; s=minimax(False); b[i]=" "
            if s<worst: worst,idx=s,i
    return idx
while True:
    show()
    p=int(input("Enter (0-8): "))
    if b[p]!=" ": print("Invalid"); continue
    b[p]="X"
    if win("X"): show(); print("Human Wins!"); break
    if " " not in b: print("Draw"); break
    b[move()]="O"
    if win("O"): show(); print("AI Wins!"); break