import sys
import os
sys.path.append(os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'Tests')))
sys.path.append("..")
sys.path.append(".")

from GraphObjs import WeightedEdge
from GraphObjs import Station
from Library.DictionaryBuilder import DictionaryBuilder
from Library.GraphBuilder import GraphBuilder
from PathFinders.AStar import AStar


graph = (GraphBuilder('_dataset/london.connections.csv', ['station1',
                      'station2', 'time'], WeightedEdge, 'undirected'))
data = '_dataset/london.stations.csv'
attribute = ['id']
type = Station
heuristic1 = 'latitude'
heuristic2 = 'longitude'
heuristic_data = DictionaryBuilder(data, attribute, type).info


def test_AStarAlgorithm_case1():
    start_node = 226
    target_node = 157
    A_Algo = AStar(graph, start_node, target_node, data,
                   attribute, type, heuristic1, heuristic2)
    distances, parent, count = A_Algo.run()
    path = A_Algo.print_path()
    assert path == [226, 127, 186, 208, 149, 162, 28, 107, 285, 279, 233, 157]
    assert count == 99


def test_AStarAlgorithm_case2():
    start_node = 100
    target_node = 11
    A_Algo = AStar(graph, start_node, target_node, data,
                   attribute, type, heuristic1, heuristic2)
    distances, parent, count = A_Algo.run()
    path = A_Algo.print_path()
    assert path == [100, 111, 22, 47, 40, 89, 277, 192, 28, 11]
    assert count == 23


def test_AStarAlgorithm_case3():
    start_node = 77
    target_node = 155
    A_Algo = AStar(graph, start_node, target_node, data,
                   attribute, type, heuristic1, heuristic2)
    distances, parent, count = A_Algo.run()
    path = A_Algo.print_path()
    assert path == [77, 124, 8, 264, 139, 40, 89, 145, 7, 188, 167, 13, 225, 155]
    assert count == 124


test_AStarAlgorithm_case1()

test_AStarAlgorithm_case2()

test_AStarAlgorithm_case3()
