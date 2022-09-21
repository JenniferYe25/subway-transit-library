from Edge import Edge
from graphBuilder import GraphBuilder

class MetricExtractor:
    def __init__(self) -> None:
        pass
    
    def total_nodes(self,graph):
            return len(graph.get_nodes())

    def total_edges(self,graph):
        nodes=graph.get_nodes()
        total_edges = 0
        for n in nodes:
            total_edges+=len(graph.get_edges(n))
        return total_edges

    def average_degree(self, graph):
        metric = MetricExtractor()
        if(graph.graph_type == "undirected"): return (metric.total_edges(graph)/2)/metric.total_nodes(graph)

        # print(metric.total_edges(graph))
        # print(metric.total_nodes(graph))
        return metric.total_edges(graph)/metric.total_nodes(graph)



metric = MetricExtractor()
graph = GraphBuilder('_dataset/test.connections.csv',['station1','station2','time'],Edge)
print(graph.graph)
print(metric.average_degree(graph))
