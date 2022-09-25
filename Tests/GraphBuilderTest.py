# from ..Library.DataExtractor import DataExtractor
from ..Library.GraphBuilder import*
from GraphObjs import Edge,WeightedEdge


GraphBuilder('_dataset/test.connections.csv',['station1','station2','time'],WeightedEdge,"undirected")
GraphBuilder('_dataset/test.connections.csv',['station1','station2'],Edge,"undirected")
