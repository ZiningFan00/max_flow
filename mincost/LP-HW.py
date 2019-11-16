import networkx as nx
import matplotlib as plt
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
        if len(lis)==0:
            break
        if lis[0]=='p':
            num=int(lis[2])
            for i in range(1,num+1):
                G.add_node(str(i))
                G.node[str(i)]['demand']=0
        if lis[0]=='n':
            n=lis[1]
            G.node[n]['demand']=int(lis[2])
        if lis[0]=='a':
            s1=lis[1]
            s2=lis[2]
            G.add_edge(s1,s2)
            G.edges[s1,s2]['capacity']=int(lis[4])
            G.edges[s1,s2]['weight']=int(lis[5])

    return(G)

G_40=create_graph('gte_bad.40')
print(nx.min_cost_flow_cost(G_40))
print("Correct value for _40 instance:", nx.flow.min_cost_flow_cost(G_40) == 52099553858)

# nx.draw(G_40)
# plt.imshow()