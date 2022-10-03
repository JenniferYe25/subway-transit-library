from GraphObjs import *
from Library.DictionaryBuilder import *
from Library.GraphBuilder import *
from PathFinders.PathFinder import PathFinder
from PathFinders.AStar import *
from Library.MetricExtractor import *
import time 

graph = (GraphBuilder('_dataset/london.connections.csv',['station1','station2','time'],WeightedEdge,'undirected'))

def test_case1():
    metric = MetricExtractor(graph)
    assert metric.total_nodes() == 302 
    assert metric.total_edges() == 812
    assert metric.average_degree() == 1.3443708609271523
    node = 11
    assert metric.degree(node) == 10 

def test_case2():
    metric = MetricExtractor(graph)
    node = 100
    assert metric.degree(node) == 2

def test_case3():
    metric = MetricExtractor(graph)
    node = 89
    assert metric.degree(node) == 6

def test_case4():
    metric = MetricExtractor(graph)
    node = 50
    assert metric.degree(node) == 1
