# from ..Library.DataExtractor import DataExtractor
from cmath import inf
from Library.GraphBuilder import*
from GraphObjs import Edge,WeightedEdge


graph = GraphBuilder('_dataset/test.connections.csv',['station1','station2','time'],WeightedEdge,"undirected")
V=max(graph.get_nodes())+1 
print(V)#call metric extraactor when imports are figured out
nodes = graph.get_nodes()
print(nodes)
# initalizaing matrix
matrix=[[None for j in range(V)]
            for i in range(V)]
# inf = no connection
# 0 = on the node
for i in nodes:
    matrix[i][i]=0
    for j in graph.graph[i]:
        node=list(j.keys())[0]
        matrix[i][node]=graph.value(i,node)
matrix=matrix[0:][1:]
print(matrix)
            
GraphBuilder('_dataset/test.connections.csv',['station1','station2'],Edge,"undirected")
