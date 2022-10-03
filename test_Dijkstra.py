from Library.GraphBuilder import GraphBuilder
from PathFinders.Dijkstra import Dijkstra
from GraphObjs import WeightedEdge


graph = (GraphBuilder('_dataset/london.connections.csv', ['station1', 'station2', 'time'], WeightedEdge, 'undirected'))


def test_DijkstraAlgorithm_case1():
    start_node, target_node = 226, 157
    D_Algo = Dijkstra(graph, start_node, target_node)
    D_Algo.run()
    assert D_Algo.return_path() == [226, 127, 186, 208, 149, 162, 28, 107, 285, 279, 233, 157]
    D_Algo.print_path()


def test_DijkstraAlgorithm_case2():
    start_node, target_node = 100, 11
    D_Algo = Dijkstra(graph, start_node, target_node)
    D_Algo.run()
    assert D_Algo.return_path() == [100, 111, 22, 47, 40, 89, 277, 192, 28, 11]
    D_Algo.print_path()


def test_DijkstraAlgorithm_case3():
    start_node, target_node = 77, 155
    D_Algo = Dijkstra(graph, start_node, target_node)
    D_Algo.run()
    assert D_Algo.return_path() == [77, 124, 8, 264, 139, 40, 89, 145, 7, 188, 167, 13, 225, 155]
    D_Algo.print_path()


test_DijkstraAlgorithm_case3()

test_DijkstraAlgorithm_case2()

test_DijkstraAlgorithm_case1()
