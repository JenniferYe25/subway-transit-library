from Library.GraphBuilder import*
from GraphObjs import Edge,WeightedEdge


def weightedEdgeGraph():
    graph = GraphBuilder('_dataset/test.connections.csv',['station1','station2','time'],WeightedEdge,"undirected")
    assert graph.get_nodes() == [1,2,3,4,5,6,7]
    assert graph.get_edges(1) == [{2: [1, '1']}, {3: [1, '2']}]
    assert graph.value(1,2) == 1 
    assert graph.value(2,1) == 1 


def unweightedEdgeGraph():
    graph = GraphBuilder('_dataset/test.connections.csv',['station1','station2'],Edge,"undirected")
    assert graph.get_nodes() == [1,2,3,4,5,6,7]

    # are strings since weight is not considered and therefore treated as a regular attribute
    assert graph.get_edges(1) == [{2: ['1', '1']}, {3: ['2', '1']}]
    assert graph.value(1,2) == '1'
    assert graph.value(2,1) == '1'
