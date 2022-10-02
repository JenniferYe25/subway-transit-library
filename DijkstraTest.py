from GraphObjs import *
from Library.DictionaryBuilder import *
from Library.GraphBuilder import *
from PathFinders.PathFinder import PathFinder
from PathFinders.Dijkstra import *
import time 

graph = (GraphBuilder('_dataset/london.connections.csv',['station1','station2','time'],WeightedEdge,'undirected'))

def test_DijkstraAlgorithm_case1():
    start_node, target_node = 226, 157
    D_Algo = Dijkstra(graph, start_node, target_node)
    num_nodes_visited = D_Algo.run()
    assert D_Algo.print_path() == [226, 127, 186, 208, 149, 162, 28, 107, 285, 279, 233, 157]
    assert num_nodes_visited == 340

def test_DijkstraAlgorithm_case2():
    start_node, target_node = 100, 11
    D_Algo = Dijkstra(graph, start_node, target_node)
    num_nodes_visited = D_Algo.run()
    assert D_Algo.print_path() == [100, 111, 22, 47, 40, 89, 277, 192, 28, 11]
    assert num_nodes_visited == 362

def test_DijkstraAlgorithm_case3():
    start_node, target_node = 77, 155
    D_Algo = Dijkstra(graph, start_node, target_node)
    num_nodes_visited = D_Algo.run()
    assert D_Algo.print_path() == [77, 124, 8, 264, 139, 40, 89, 145, 7, 188, 167, 13, 225, 155]
    assert num_nodes_visited == 363
