import networkx as nx

graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

G = nx.DiGraph()

for u in graph.keys():
    for v in graph[u]:
        G.add_edge(u,v)

# G=nx.DiGraph()

for neighbor in G.neighbors('11'):
    print("a")

def bfs(graph):
    paths = []
    stpath=[]
    paths.append('8')
    while paths:
        path = paths.pop(0)
        node = path[-1]
        if node == 't':
            for i in range(0,len(path)-1):
                stpath.append([path[i],path[i+1]])
            return(stpath)
        for neighbor in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            paths.append(new_path)
    
    return()

print(bfs(graph))