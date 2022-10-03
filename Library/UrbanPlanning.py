from Library.GraphBuilder import GraphBuilder
from Library.DictionaryBuilder import DictionaryBuilder
from GraphObjs import Station
from GraphObjs import WeightedEdge


class UrbanPlanning():

    def __init__(self, graph):
        self.graph = graph
        self.node_to_otherzone = []
        self.nodes = graph.get_nodes()
        self.zoneDict = {}
        self.nodes_touched = 0
        self.dictBuild = DictionaryBuilder('_dataset/london.stations.csv', ['id'], Station).info
        self.stations = list(self.dictBuild.keys())
        self.islands = [[] for i in range(len(self.stations) + 2)]

    def get_adj_node(self, node):
        graphBuilder = GraphBuilder('_dataset/london.connections.csv', ['station1', 'station2', 'time'], WeightedEdge, "undirected")
        graph = graphBuilder.graph
        values = graph[node]
        adj = []
        for j in range(len(values)):
            adj.append(list(values[j].keys())[0])
        return adj

    def DFSUtil(self, temp, nodes, zone):
        self.visited[temp] = True
        nodes.append(temp)
        fromnode = temp
        adj_list = self.get_adj_node(fromnode)
        for i in adj_list:
            self.nodes_touched += 1
            if self.visited[i] is False and self.dictBuild[i]['zone'] == zone:
                nodes = self.DFSUtil(i, nodes, zone)
            zone_connect = [(temp, self.dictBuild[temp]['zone']), (i, self.dictBuild[i]['zone'])]
            if not self.visited[i] and self.dictBuild[i]['zone'] != zone and nodes not in self.node_to_otherzone:
                self.node_to_otherzone.append(zone_connect)
        return nodes

    def get_zone_to_zone(self):
        return self.node_to_otherzone

    def get_num_of_nodes_touched(self):
        return self.nodes_touched - 194

    def Zone(self):
        self.visited = []
        for i in range(len(self.stations)+2):
            self.visited.append(False)
        for key in self.stations:
            if key != 189:
                self.zoneDict[self.dictBuild[key]['zone']] = []
        for key in self.stations:
            self.zoneDict[self.dictBuild[key]['zone']].append(key)

        for i in self.zoneDict:
            for j in range(len(self.zoneDict[i])):
                if self.visited[self.zoneDict[i][j]] is False:
                    nodes = []
                    print(self.DFSUtil(self.zoneDict[i][j], nodes, i))

                    self.islands[self.zoneDict[i][j]] = (self.DFSUtil(self.zoneDict[i][j], nodes, i))
        self.islands = [island for island in self.islands if island != []]
        Empty = []
        for i in range(len(self.islands)):
            Empty.append([])
        for i in range(len(self.islands)):
            for dupe in self.islands[i]:
                if dupe not in Empty[i]:
                    Empty[i].append(dupe)

        self.islands = Empty
        return self.islands

