class MetricExtractor:
    def __init__(self, graph) -> None:
        self.graph = graph

    def total_nodes(self):
        return len(self.graph.get_nodes())

    def total_edges(self):
        nodes = self.graph.get_nodes()
        total_edges = 0
        for n in nodes:
            total_edges += len(self.graph.get_edges(n))
        return total_edges

    def average_degree(self):
        metric = MetricExtractor(self.graph)
        if (self.graph.graph_type == "undirected"): return (metric.total_edges()/2)/metric.total_nodes()
        return metric.total_edges() / metric.total_nodes()

    def degree(self, node):
        degree = len(self.graph.get_edges(node))
        return degree
