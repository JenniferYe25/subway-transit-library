from itertools import count
from GraphObjs import *
from Library.DictionaryBuilder import *
from Library.GraphBuilder import *
from PathFinders.PathFinder import PathFinder
from PathFinders.AStar import *
import time 

# inputting data as file, attribute as id, and type as Station to receive node data. 
# in real usage, would ask for input for these parameters from users, in the case the data info needed to be extracted is different.
def testAStar():
    graph = (GraphBuilder('_dataset/london.connections.csv',['station1','station2','time'],WeightedEdge,'undirected'))
    start = time.time()
    A_Algo = AStar(graph,226,157,'_dataset/london.stations.csv',['id'],Station,'latitude','longitude')
    distances,parent,count = A_Algo.run()
    path = A_Algo.print_path()
    end = time.time()
    print(end-start)

testAStar()