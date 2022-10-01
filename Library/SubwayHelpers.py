from PathFinders.Dijkstra import Dijkstra


# contructor converts adj list to matrix
def convert_to_matrix(graph, checkpoint):
    # initalizaing matrix
    V=max(graph.get_nodes())+1 
    nodes = graph.get_nodes()
    # fill matrix with values of each row as start, each col is distnce from start to it
    matrix=[[0 for j in range(V)] for i in range(V)]

    for j in range(len(checkpoint)):
        d=Dijkstra(graph,checkpoint[j], checkpoint[j]) #target param is ignored 
        d.run()
        temp=d.return_total_weight()
        temp_keys=temp.keys()
        for i in temp_keys:
            matrix[checkpoint[j]][i]=temp.get(i)
    return matrix


def find_path(graph, checkpoint):
    path=[]
    for i in range(len(checkpoint)-1): #go through each point in temp list
        d=Dijkstra(graph,checkpoint[i], checkpoint[i+1])
        d.run()
        path.append(d.return_path())

    return path
