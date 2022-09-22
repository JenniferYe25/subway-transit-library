from GraphObjects.Edge import*
from GraphBuilder import GraphBuilder


GraphBuilder('_dataset/test.connections.csv',['station1','station2','time'],WeightedEdge,"undirected")
GraphBuilder('_dataset/test.connections.csv',['station1','station2'],Edge,"undirected")
