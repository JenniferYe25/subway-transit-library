from Library.DataExtractor import *
from Library.GraphBuilder import *
from Library.GraphBuilder import *
from Library.SubwayPatrol import *
from GraphObjs import *
from PathFinders.AStar import *
from PathFinders.Dijkstra import*

def testDataExtrcator():
    print("Testing Data Extractor")
    data=DataExtractor()
    data.extractRows('_dataset/london.connections.csv',['station1', 'station2', 'time'], WeightedEdge)
    data.extractRows('_dataset/london.stations.csv',['id'],Station)

def testGraphBuilder():
    print("Testing Graph Builder")
    GraphBuilder('_dataset/test.connections.csv',['station1','station2','time'],WeightedEdge,"undirected")
    GraphBuilder('_dataset/test.connections.csv',['station1','station2'],Edge,"undirected")

def testDictionaryBuilder():
    print(DictionaryBuilder('_dataset/london.stations.csv',['id'],Station).info)

def testDijkstra():
    # graph=(GraphBuilder('_dataset/test.connections.csv',['station1','station2','time'],WeightedEdge,"undirected"))
    # d = Dijkstra(graph, 1, 7)
    # d.run()
    # d.print_path()
    # d.return_total_weight()

    graph=(GraphBuilder('_dataset/london.connections.csv',['station1','station2','time'],WeightedEdge,"undirected"))
    total=0
    d = Dijkstra(graph, 1, 193)
    d.run()
    # d.print_path()
    print(d.return_total_weight()[193])

    d = Dijkstra(graph, 193, 266)
    d.run()
    # d.print_path()
    print(d.return_total_weight()[266])

    d = Dijkstra(graph, 266, 94)
    d.run()
    # d.print_path()
    print(d.return_total_weight()[94])

    d = Dijkstra(graph, 94, 235)
    d.run()
    # d.print_path()
    print(d.return_total_weight()[235])

    d = Dijkstra(graph, 235,1)
    d.run()
    # d.print_path()
    print(d.return_total_weight()[1])
    # print(total)

def testSubwayPatrol():
    graph=GraphBuilder('_dataset/london.connections.csv',['station1','station2','time'],WeightedEdge,"undirected")
    subway=SubwayPatrol(graph)
    # for i in subway.matrix:
    #     print(i)
    # count=0
    # print(subway.run([1,94,235,193,266]))
    # for i in subway.run([1,94,235,193,266]):
    #     print(i)
        # count+=len(i)
    # print(count)
    # temp=[[1, 73, 182, 194, 5, 252, 251, 235], [235, 210, 291, 115, 178, 202, 282, 94], [94, 11, 104, 90, 145, 123, 95, 160, 266], [266, 160, 95, 123, 145, 90, 104, 11, 83, 193], [193, 218, 283, 147, 150, 227, 101, 110, 265, 1]]
    # count=0
    # for i in temp:
    #     count+=len(i)
    # print(count)
    print(subway.run([1,94,235,193,266]))
    # assert subway.get_value(1,2) == 1
    # assert subway.get_value(1,1) == 0 
    # assert subway.get_value(7,5) == 2

    # graph=GraphBuilder('_dataset/test.connections.csv',['station1','station2','time'],WeightedEdge,"undirected")
    # subway=SubwayPatrol(graph)
    # print(subway.run([3,6,7,2]))


def testAStar():
    graph = (GraphBuilder('_dataset/london.connections.csv',['station1','station2','time'],Connection,'undirected'))
    start = '100'
    target = '11'

    A_Algo = AStar(graph,'100','11')
    distances,parent = A_Algo.run()
    Path=A_Algo.print_path()
    print(Path)



# testDictionaryBuilder()
testSubwayPatrol()
# testDijkstra()