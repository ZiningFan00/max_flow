graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

def bfs(graph, start, end):
    paths = []
    stpath=[]
    paths.append('s')
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

print(bfs(graph, '1', '11'))