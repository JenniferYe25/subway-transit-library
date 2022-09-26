from ..GraphObjs import *
from Library.GraphBuilder import *

class MetricExtractor:
    def __init__(self,graph,node) -> None:
        self.graph=graph
        self.node=node
    
    def total_nodes(self):
            return len(self.graph.get_nodes())

    def total_edges(self):
        nodes=self.graph.get_nodes()
        total_edges = 0
        for n in nodes:
            total_edges+=len(self.graph.get_edges(n))
        return total_edges

    def average_degree(self):
        metric = MetricExtractor()
        if(self.graph.graph_type == "undirected"): return (metric.total_edges(graph)/2)/metric.total_nodes(graph)
        return metric.total_edges(self.graph)/metric.total_nodes(self.graph)
        
    def degree(self):
        degree= len(self.graph.get_edges(self.node))
        return degree

graph = GraphBuilder('_dataset/london.connections.csv',['station1','station2','time'],WeightedEdge,"undirected")
