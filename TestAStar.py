from GraphObjs import *
from Library.DictionaryBuilder import *
from Library.GraphBuilder import *
from PathFinders.PathFinder import PathFinder
from PathFinders.AStar import *

# inputting data as file, attribute as id, and type as Station to receive node data. 
# in real usage, would ask for input for these parameters from users, in the case the data info needed to be extracted is different.
def testAStar():
    graph = (GraphBuilder('_dataset/london.connections.csv',['station1','station2','time'],WeightedEdge,'undirected'))
    A_Algo = AStar(graph,1,7,'_dataset/london.stations.csv',['id'],Station,'latitude','longitude')
    distances,parent = A_Algo.run()
    A_Algo.print_path()

testAStar()