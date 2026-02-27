import networkx as nx
import matplotlib.pyplot as plt

class CSP:
    def __init__(self, vars, doms, cons):
        self.vars, self.doms, self.cons = vars, doms, cons
    def consistent(self, v, val, assign):
        return all(c(v, val, assign) for c in self.cons.get(v, []))
    def backtrack(self, assign={}):
        if len(assign) == len(self.vars): return assign
        v = next(x for x in self.vars if x not in assign)
        for val in self.doms[v]:
            if self.consistent(v, val, assign):
                assign[v] = val
                res = self.backtrack(assign)
                if res: return res
                assign.pop(v)
        return None

vars = ['A','B','C']
doms = {v:[1,2,3] for v in vars}
cons = {
    'A':[lambda v,val,a:'B' not in a or a['B']!=val],
    'B':[lambda v,val,a:'A' not in a or a['A']!=val],
    'C':[lambda v,val,a:'A' not in a or a['A']!=val,
         lambda v,val,a:'B' not in a or a['B']!=val]
}

csp = CSP(vars, doms, cons)
sol = csp.backtrack()
print("Solution:", sol)

G = nx.Graph()
G.add_nodes_from(vars)
G.add_edges_from([('A','B'),('A','C'),('B','C')])
colors = ['red' if sol[n]==1 else 'green' if sol[n]==2 else 'blue' for n in G]
nx.draw(G, with_labels=True, node_color=colors, node_size=2000, font_weight='bold')
plt.show()