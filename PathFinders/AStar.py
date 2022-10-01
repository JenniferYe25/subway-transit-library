import sys, os
sys.path.append(os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),'..','PathFinders')))
sys.path.append("..")
sys.path.append(".")

from GraphObjs import *
from Library.DictionaryBuilder import *
from Library.GraphBuilder import *
from PathFinder import PathFinder


import heapq

class AStar(PathFinder):
    def __init__(self, graph, start, target,data,attribute,type,heuristic1,heuristic2) -> None:
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
     

    def run(self):
        visited = set()
        prev_line=list(self.graph.get_edges(self.start)[0].items())[0][1][0]
        pq = [(AStar.calculate_heuristic(self.start,self.target,self.data,self.attribute,self.type,self.heuristic1,self.heuristic2), 0 ,  self.start)] 

        count = 0
        while pq:
            count +=1
            curr_f, curr_dist, curr_vert = heapq.heappop(pq) 

            if curr_vert not in visited:
                visited.add(curr_vert)

                for connection in self.graph.get_edges(curr_vert):
                    neighbor=list(connection.keys())[0]
                    weight=list(connection.values())[0][0]
                    current_line=list(connection.values())[0][1]
                    distance = curr_dist + weight  # distance from start (g)

                    f_distance = distance + AStar.calculate_heuristic(self.start,neighbor,self.data,self.attribute,self.type,self.heuristic1,self.heuristic2) # f = g + h

                    if prev_line != current_line:
                        distance+=0.5

                    # Only process new vert if it's f_distance is lower
                    if f_distance < self.distances[neighbor]:
                        self.distances[neighbor] = f_distance
                        self.parent[neighbor] = curr_vert

                        if neighbor == self.target:
                            # we found a path based on heuristic
                            return self.distances, self.parent,count
                        heapq.heappush(pq, (f_distance, distance, neighbor)) 
        # print('distance' ,distance, 'parent:' , parent)
        return self.distances, self.parent, count


    def print_path(self):
        current = self.target

        while current:
            self.path.append(current)
            current = self.parent[current]
        self.path = self.path[::-1]
        print("path from", self.start, "to", self.target)
        print_path=""
        for node in self.path[:-1]:
            print_path+=str(node)+" -> "
        print(print_path+str(self.path[-1]))


    def calculate_heuristic(start, target,data,attribute,type,heuristic1,heuristic2,):
            node1x, node1y = DictionaryBuilder(data,attribute,type).info[start][heuristic1], DictionaryBuilder(data,attribute,type).info[start][heuristic2]
            node2x, node2y = DictionaryBuilder(data,attribute,type).info[target][heuristic1] , DictionaryBuilder(data,attribute,type).info[target][heuristic2]
            heuristic = abs(float(node1x) - float(node2x)) + \
                abs(float(node1y) - float(node2y))
            return 100*heuristic

