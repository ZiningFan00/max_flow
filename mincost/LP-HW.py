import networkx as nx
import pulp
def create_graph(infile):
    """Creates a directed graph as specified by the input file. Edges are annotated with 'capacity'
    and 'weight' attributes, and nodes are annotated with 'demand' attributes.
    
    Args:
        infile: the input file using the format to specify a min-cost flow problem.
        
    Returns:
        A directed graph (but not a multi-graph) with edges annotated with 'capacity' and 'weight' attributes
        and nodes annotated with 'demand' attributes.
    """
    # TODO: implement function
    G=nx.MultiDiGraph()

    f = open(infile)
    for line in f:
        lis=line.strip().split()
        if len(lis)==0:
            break
        if lis[0]=='p':
            num=int(lis[2])
            for i in range(1,num+1):
                G.add_node(str(i))
                G.node[str(i)]['demand']=0
        if lis[0]=='n':
            n=lis[1]
            G.node[n]['demand']=float(lis[2])
        if lis[0]=='a':
            s1=lis[1]
            s2=lis[2]
            G.add_edge(s1,s2,capacity=float(lis[4]),weight=float(lis[5]))
    
    return(G)

# def lp_flow_value(G):
    
#     # reduce multigraph to simple graph
#     for s1,s2 in G.edges():
#         if len(G.adj[s1][s2])>1:
            
#         print(G.adj[s1][s2])
#         a=1

G_40 = create_graph('mincost/gte_bad.40')
flow=nx.min_cost_flow(G_40,demand='demand',capacity='capacity',weight='weight')
a=0