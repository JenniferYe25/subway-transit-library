from multiprocessing import connection
from Connection import Connection
from DataExtractor import DataExtractor

class GraphBuilder:
    def __init__(self, lines, stations, connections) -> None:
        data_extractor=DataExtractor()
        self.lines=data_extractor.LinesBuilding(lines)
        self.stations=data_extractor.StationsBuilding(stations)
        self.adj=data_extractor.ConnectionBuilding(connections)
        
        v = set()
        for key in self.adj:
            v.add(key)
            for connection in self.adj[key]:
                v.add(Connection.get_station2)

        self.vertices=len(v)

        e=0
        for key in self.adj:
            e+=len(self.adj[key])
        self.edges=e
        



        
    


graph=GraphBuilder('_dataset/london.lines.csv','_dataset/london.stations.csv', '_dataset/london.connections.csv')
print(graph.)