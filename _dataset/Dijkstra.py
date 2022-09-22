import heapq
from importlib.resources import path

from graphBuilder import GraphBuilder
from Edge import WeightedEdge

class Dijkstra:
    def __init__(self, graph, start_node, target_node) -> None:
        self.distances = {vertex: float('inf') for vertex in graph.get_nodes()}
        self.distances[start_node] = 0
        self.parent = {vertex: None for vertex in graph.get_nodes()} # store path 
        self.start = start_node
        self.target = target_node

        prev_line=list(graph.get_edges(start_node)[0].items())[0][1][0]

        pq = [(0, start_node)]
        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > self.distances[current_vertex]:
                continue
           
            for connection in graph.get_edges(current_vertex):
                values=list(connection.values())
                neighbor=list(connection.keys())[0]
                weight=values[0][0]
                current_line=values[0][1]

                distance = current_distance + weight
                if prev_line != current_line:
                    distance+=0.5

                if distance < self.distances[neighbor]:
                    self.distances[neighbor] = distance
                    self.parent[neighbor]=current_vertex
                prev_line=current_line
                heapq.heappush(pq, (distance, neighbor))

        self.path = []
        current = target_node

        while current:
            self.path.append(current)
            current = self.parent[current]
        
    
    def print_path(self):
        self.path = self.path [::-1]
        print("path from ", self.start, " to  ", self.target)
        print_path=""
        for node in self.path[:-1]:
            print_path+=str(node)+" -> "
        print(print_path+str(self.path[-1]))


graph=(GraphBuilder('_dataset/test.connections.csv',['station1','station2','time'],WeightedEdge,"undirected"))

# graph=(GraphBuilder('_dataset/test.graph.csv',["start","end","weight"],Connection))
# print(graph.graph)
# print(graph.get_nodes())
d = Dijkstra(graph, 1, 7)
d.print_path()

