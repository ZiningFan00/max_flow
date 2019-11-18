import networkx as nx
G=nx.DiGraph()
G.add_node('u')
G.add_node('v')
G.add_node('uv')
G.add_edge('u','uv',capacity=1)
G.add_edge('uv','v',capacity=2)
a=0
