from graphBuilder import GraphBuilder
from Connection import Connection 
from Station import Station
from DictionaryBuilder import DictionaryBuilder
from Edge import *
import heapq

class AStar:
    def __init__(self, graph, start, dest) -> None:
        self.distances = {vertex: float('inf') for vertex in graph.get_nodes()}
        self.distances[start] = 0
        self.parent = {vertex: None for vertex in graph.get_nodes()} # store path 
        self.start = start
        self.dest = dest

    def run(self):
        visited = set()
        prev_line=list(graph.get_edges(start)[0].items())[0][1][0]
        pq = [(AStar.calculate_heuristic(start,dest), 0 ,  start)] 

        while pq: 
            curr_f, curr_dist, curr_vert = heapq.heappop(pq) 

            if curr_vert not in visited:
                visited.add(curr_vert)

                for connection in graph.get_edges(curr_vert):
                    neighbor=list(connection.keys())[0]
                    weight=list(connection.values())[0][0]
                    current_line=list(connection.values())[0][1]
                    distance = curr_dist + weight  # distance from start (g)

                    f_distance = distance + AStar.calculate_heuristic(start,neighbor) # f = g + h

                    if prev_line != current_line:
                        distance+=0.5

                    # Only process new vert if it's f_distance is lower
                    if f_distance < self.distances[neighbor]:
                        self.distances[neighbor] = f_distance
                        self.parent[neighbor] = curr_vert

                        if neighbor == dest:
                            # we found a path based on heuristic
                            return self.distances, self.parent
                        heapq.heappush(pq, (f_distance, distance, neighbor)) 
        # print('distance' ,distance, 'parent:' , parent)
        return distances, parent


    def generate_path_from_parents(self):
        path = []
        curr = self.dest
        while curr:
            path.append(curr)
            curr = self.parent[curr]
        return 'optimal path is: ', '->'.join(path[::-1])


    def calculate_heuristic(start, dest):

            node1x, node1y = DictionaryBuilder('_dataset/london.stations.csv',['id'],Station).info[start]['latitude'], DictionaryBuilder('_dataset/london.stations.csv',['id'],Station).info[start]['longitude']
            node2x, node2y = DictionaryBuilder('_dataset/london.stations.csv',['id'],Station).info[dest]['latitude'] , DictionaryBuilder('_dataset/london.stations.csv',['id'],Station).info[dest]['longitude']
            heuristic = abs(float(node1x) - float(node2x)) + \
                abs(float(node1y) - float(node2y))
            return 100*heuristic

graph = (GraphBuilder('_dataset/london.connections.csv',['station1','station2','time'],Connection,'undirected'))
start = '100'
dest = '11'

A_Algo = AStar(graph,'100','11')
distances,parent = A_Algo.run()
Path=A_Algo.generate_path_from_parents()
print(Path)
