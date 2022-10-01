from itertools import permutations
from math import inf
from Library.SubwayHelpers import *

class SubwayPatrol:
    # checkpoints - array of station numbers
    def __init__(self, graph) -> None:
        self.graph=graph

    def run(self, checkpoints):
        check=all(point in self.graph.get_nodes() for point in checkpoints)
        if check==False:
            return "A station does not exist on the map"

        # initalizing
        matrix = convert_to_matrix(self.graph, checkpoints)
        final_weight = inf
        temp_weight=0
        path=[]

        perm=list(permutations(checkpoints))
        for i in perm:
            i+=(i[0],) #adding start point as last point to create a cycle
            point = 0
            temp_weight=0
            for j in i:
                temp_weight+=matrix[point][j]
                point = j
            if(temp_weight < final_weight):
                # print(i, temp_weight, final_weight)
                final_weight=temp_weight
                points=list(i)

        path=find_path(self.graph, points)
        return path 
            
            

        







     
