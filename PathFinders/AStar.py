import sys
import os
sys.path.append(os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'PathFinders')))
sys.path.append("..")
sys.path.append(".")

from Library.DictionaryBuilder import DictionaryBuilder
from PathFinder import PathFinder
import heapq


class AStar(PathFinder):

    def __init__(self, graph, start, target, data, attribute, type, heuristic1, heuristic2):
        super().__init__(graph, start, target)
        self.path = []
        # data file
        self.data = data
        # file value (e.g 'id')
        self.attribute = attribute
        # type of data e.g Station
        self.type = type
        self.heuristic1 = heuristic1
        self.heuristic2 = heuristic2
        self.heuristic_data = DictionaryBuilder(data, attribute, type).info

    def run(self):
        visited = set()
        prev_line = list(self.graph.get_edges(self.start)[0].items())[0][1][0]
        heuristic = AStar.calculate_heuristic(self.heuristic_data, self.start, self.target, self.heuristic1, self.heuristic2), 0, self.start
        pq = [heuristic]

        count = 0
        while pq:
            count += 1
            curr_f, curr_dist, curr_vert = heapq.heappop(pq)

            if curr_vert not in visited:
                visited.add(curr_vert)

                for connection in self.graph.get_edges(curr_vert):
                    neighbor = list(connection.keys())[0]
                    weight = list(connection.values())[0][0]
                    current_line = list(connection.values())[0][1]
                    distance = curr_dist + weight  # distance from start (g)

                    heuristic = AStar.calculate_heuristic(self.heuristic_data, self.start, neighbor, self.heuristic1, self.heuristic2)
                    f_distance = distance + heuristic  # f = g + h

                    if prev_line != current_line:
                        distance += 0.5

                    # Only process new vert if it's f_distance is lower
                    if f_distance < self.distances[neighbor]:
                        self.distances[neighbor] = f_distance
                        self.parent[neighbor] = curr_vert

                        if neighbor == self.target:
                            # we found a path based on heuristic
                            return self.distances, self.parent, count
                        heapq.heappush(pq, (f_distance, distance, neighbor))
        return self.distances, self.parent, count

    def print_path(self):
        current = self.target

        while current:
            self.path.append(current)
            current = self.parent[current]
        self.path = self.path[::-1]
        print_path = []
        for node in self.path[:-1]:
            print_path.append(node)
        print_path.append(self.path[-1])
        return print_path

    def calculate_heuristic(dictionary, start, target, heuristic1, heuristic2):
        node1x = dictionary[start][heuristic1]
        node1y = dictionary[start][heuristic2]
        node2x = dictionary[target][heuristic1]
        node2y = dictionary[target][heuristic2]
        heuristic = abs(float(node1x) - float(node2x)) + \
            abs(float(node1y) - float(node2y))
        return 100*heuristic
