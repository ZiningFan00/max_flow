import networkx as nx
import matplotlib.pyplot as plt

graph = {
        's': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['t', '12']
        }

G = nx.DiGraph()

for u in graph.keys():
    for v in graph[u]:
        G.add_edge(u,v)

# G = nx.DiGraph(G)

def dfs(graphR):

    s=[]
    s.append('9')
    visited=[]
    prev={}

    while len(s)>0:
        u=s.pop()   
        if u not in visited:
            visited.append(u)
            for neighbor in sorted(graphR.neighbors(u)):
                if neighbor not in visited:
                    d={neighbor:u}
                    prev.update(d)
                    s.append(neighbor)
    
    if 't' not in prev.keys():
        return()
    else:
        path=[]
        l=[]
        l.append([prev['t'],'t'])
        while len(l)>0:
            e=l.pop()
            path.append(e)
            if e[0]=='s':
                return(path)
            else:
                l.append([prev[e[0]],e[0]])

print(dfs(G))