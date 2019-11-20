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
            s3='u'+s1+s2
            if s3 in G.nodes():
                s3='v'+s1+s2
            G.add_node(s3,demand=0)
            G.add_edge(s1,s3,capacity=int(lis[4]),weight=int(lis[5]))
            G.add_edge(s3,s2,capacity=int(lis[4]),weight=0)

    return(G)

def lp_flow_value(G):
    LP = pulp.LpProblem("My LP Problem", pulp.LpMinimize)
    flow=[]
    ob_func=0

    for node in G.nodes():
        G.nodes[node]['in']=0
        G.nodes[node]['out']=0
    
    for s1,s2 in G.edges():
        flow.append(pulp.LpVariable(s1+'_'+s2,lowBound=0,upBound=G.edges[s1,s2]['capacity'],cat='Continuous'))

    for edge in flow:
        s1,s2=str(edge).split('_')
        ob_func=ob_func+G.edges[s1,s2]['weight']*edge
        G.node[s1]['out']=G.node[s1]['out']+edge
        G.node[s2]['in']=G.node[s2]['in']+edge
    
    LP += ob_func
    for node in G.nodes():
        LP += G.nodes[node]['demand']==G.nodes[node]['in']-G.nodes[node]['out']
    
    LP.solve()
    return(int(pulp.value(LP.objective)))
    
G_40 = create_graph('mincost/gte_bad.40')
print(lp_flow_value(G_40))
print( "Correct value for _40 instance:", lp_flow_value(G_40) == 52099553858)
print(nx.flow.min_cost_flow_cost(G_40))
print("Correct value for _40 instance:", nx.flow.min_cost_flow_cost(G_40) == 52099553858)
