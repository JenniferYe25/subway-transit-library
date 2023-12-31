import heapq
import sys
import os
sys.path.append(os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'PathFinders')))
sys.path.append("..")
sys.path.append(".")

from PathFinder import PathFinder


class Dijkstra(PathFinder):

    def __init__(self, graph, start_node, target_node) -> None:
        super().__init__(graph, start_node, target_node)
        self.path = []

    def run(self):
        prev_line = list(self.graph.get_edges(self.start)[0].items())[0][1][0]

        pq = [(0, self.start)]
        counter = 0
        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > self.distances[current_vertex]:
                continue

            for connection in self.graph.get_edges(current_vertex):
                values = list(connection.values())
                neighbor = list(connection.keys())[0]
                weight = values[0][0]
                current_line = values[0][1]

                distance = current_distance + weight
                if prev_line != current_line:
                    distance += 0.5

                if distance < self.distances[neighbor]:
                    self.distances[neighbor] = distance
                    self.parent[neighbor] = current_vertex
                    counter += 1
                prev_line = current_line
                heapq.heappush(pq, (distance, neighbor))

    def print_path(self):
        current = self.target
        while current:
            self.path.append(current)
            try:
                current = self.parent[current]
            except:
                print("Can't reach the target from the starting node")
                return

        self.path = self.path[::-1]
        print("path from", self.start, "to", self.target)
        print_path = ""
        for node in self.path[:-1]:
            print_path += str(node)+" -> "
        print(print_path+str(self.path[-1]))

    def return_path(self):
        current = self.target
        while current:
            self.path.append(current)
            try:
                current = self.parent[current]
            except:
                return None
    
        self.path = self.path[::-1]
        print_path = []
        for node in self.path[:-1]:
            print_path.append(node)
        print_path.append(self.path[-1])
        return print_path

    def return_total_weight(self):
        return self.distances
