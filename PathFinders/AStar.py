from DictionaryBuilder import DictionaryBuilder
from ..GraphObjs import *

import heapq

def a_star(graph, start, dest):
    distances = {vertex: float('inf') for vertex in graph.get_nodes()} 
    distances[start] = 0

    parent = {vertex: None for vertex in graph.get_nodes()} # store path 
    visited = set()
    pq = [( calculate_heuristic(start,dest), 0 ,  start)] 

    while pq: 
        curr_f, curr_dist, curr_vert = heapq.heappop(pq) 

        if curr_vert not in visited:
            visited.add(curr_vert)

            for connection in graph.get_edges(curr_vert):
                neighbor=list(connection.keys())[0]
                weight=list(connection.values())[0][0]
                distance = curr_dist + weight  # distance from start (g)

                f_distance = distance + calculate_heuristic(start,neighbor) # f = g + h

                # Only process new vert if it's f_distance is lower
                if f_distance < distances[neighbor]:
                    distances[neighbor] = f_distance
                    parent[neighbor] = curr_vert

                    if neighbor == dest:
                        # we found a path based on heuristic
                        return distances, parent
                    heapq.heappush(pq, (f_distance, distance, neighbor)) 
    # print('distance' ,distance, 'parent:' , parent)
    return distances, parent


def generate_path_from_parents(parent, start, dest):
    path = []
    curr = dest
    while curr:
        path.append(curr)
        curr = parent[curr]

    return '->'.join(path[::-1])


def calculate_heuristic(start, dest):
        node1x, node1y = DictionaryBuilder('_dataset/london.stations.csv',['id'],Station).info[start]['latitude'], DictionaryBuilder('_dataset/london.stations.csv',['id'],Station).info[start]['longitude']
        node2x, node2y = DictionaryBuilder('_dataset/london.stations.csv',['id'],Station).info[dest]['latitude'] , DictionaryBuilder('_dataset/london.stations.csv',['id'],Station).info[dest]['longitude']
        heuristic = abs(float(node1x) - float(node2x)) + \
            abs(float(node1y) - float(node2y))
        return 100*heuristic




