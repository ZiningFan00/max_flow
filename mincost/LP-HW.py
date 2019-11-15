import networkx as nx
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
    G=nx.DiGraph()

    f = open(infile)
    for line in f:
        lis=line.strip().split()
        if lis[0]=='n':
            n=lis[1]
            G.add_node(n)
            G.node[n]['demand']=int(lis[2])
        # if lis[0]=='a':
        #     s1=
        #     s2=
        #     G.add_edge(lis[1],lis[2])
        #     G.edges[lis[1],lis[2]]['capacity']=int(lis[4])
        #     G.edges[lis[1],lis[2]]['cost']=int(lis[5])

        # if lis[0]=='a':
        #     G.add_edge

    return(G)


G_40=create_graph('gte_bad.40')