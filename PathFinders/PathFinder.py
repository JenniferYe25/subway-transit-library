from abc import ABC, abstractmethod

class PathFinder(ABC):
    def __init__(self, graph, start_node, target_node) -> None:
            self.graph=graph
            self.distances = {vertex: float('inf') for vertex in graph.get_nodes()}
            self.distances[start_node] = 0
            self.parent = {vertex: None for vertex in graph.get_nodes()} # store path 
            self.start = start_node
            self.target = target_node

    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def print_path(self):
        pass