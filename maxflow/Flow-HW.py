import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

usa = open('contiguous-usa.dat')
for line in usa:
    s1, s2 = line.strip().split()
    G.add_edge(s1, s2)

for state in G.nodes():
    if state != 'CA':
        G.node[state]['demand'] = 1
G.node['CA']['demand'] = -48

G = nx.DiGraph(G)
uniform_capacity = 16
for (s1, s2) in G.edges():
    G.edges[s1, s2]['capacity'] = uniform_capacity

def flow_with_demands(graph):
    """Computes a flow with demands over the given graph.
    
    Args:
        graph: A directed graph with nodes annotated with 'demand' properties and edges annotated with 'capacity' 
            properties.
        
    Returns:
        A dict of dicts containing the flow on each edge. For instance, flow[s1][s2] should provide the flow along
        edge (s1, s2).
        
    Raises:
        NetworkXUnfeasible: An error is thrown if there is no flow satisfying the demands.
    """
    # TODO: Implement the function.
    
    # add super source node and super sink node 
    graphNew=graph.copy()

    graphNew.add_node('s')
    graphNew.add_node('t')
    graphNew.node['s']['demand'] = 0
    graphNew.node['t']['demand'] = 0   
    
    f=0
    
    # add adajcent edges and assign capacities
    for state in graphNew.nodes():
        d=graphNew.node[state]['demand']
        if d < 0:
            graphNew.add_edge('s',state)
            graphNew.edges['s',state]['capacity']=-d
            # compute the sum of demands 
            f=f-d
        if d > 0:
            graphNew.add_edge(state,'t')
            graphNew.edges[state,'t']['capacity']=d
    
    flow_value, flow_dict = nx.maximum_flow(graphNew, 's', 't',capacity='capacity')
    
    del flow_dict['s']
    del flow_dict['t']
    
    for s1 in list(flow_dict):
        for s2 in list(flow_dict[s1]):
            if s2 =='t':
                del flow_dict[s1]['t']

    if flow_value == f:
        return(flow_dict)
    else:
        raise ValueError('NetworkXUnfeasible')

def divergence(flow):
    """Computes the total flow into each node according to the given flow dict.
    
    Args:
        flow: the flow dict recording flow between nodes.
        
    Returns:
        A dict of the net flow into each node.
    """
    # TODO: Implement the function.
    
    div=dict()
    for state in flow.keys():
        div[state]=0

    for s1 in div.keys():
        for s2 in flow[s1].keys():
            div[s1]=div[s1]-flow[s1][s2]
            div[s2]=div[s2]+flow[s1][s2]

    return(div)

flow=flow_with_demands(G)
print(flow)
div=divergence(flow)
print(div)