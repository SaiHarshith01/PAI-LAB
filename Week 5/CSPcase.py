import networkx as nx
import matplotlib.pyplot as plt

class CSP:
    def __init__(self, vars, doms, cons): self.vars, self.doms, self.cons = vars, doms, cons
    def consistent(self, v,val,assign): return all(c(v,val,assign) for c in self.cons.get(v,[]))
    def backtrack(self, assign={}):
        if len(assign)==len(self.vars): return assign
        v = next(x for x in self.vars if x not in assign)
        for val in self.doms[v]:
            if self.consistent(v,val,assign):
                assign[v]=val
                res=self.backtrack(assign)
                if res: return res
                assign.pop(v)
        return None

exams = ['E1','E2','E3']
proctors = ['P1','P2','P3']
domains = {'E1':['P1','P2'], 'E2':['P1','P3'], 'E3':['P1','P2']}
constraints = {e:[lambda v,val,a: val not in a.values()] for e in exams}

csp = CSP(exams, domains, constraints)
sol = csp.backtrack()
print("Solution:", sol)

G = nx.Graph()
G.add_nodes_from(exams+proctors)
for e,p in sol.items(): G.add_edge(e,p)
colors=['lightblue' if n in exams else 'lightgreen' for n in G.nodes()]
nx.draw(G, nx.spring_layout(G), with_labels=True, node_color=colors, node_size=2000, font_weight='bold')
plt.show()