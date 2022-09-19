from DataExtractor import DataExtractor
from Connection import Connection
from Station import Station

class GraphBuilder:
    def __init__(self,path,required,edge_type,graph_type):
        data=DataExtractor()
        data_obj=data.extractRows(path,required,edge_type)
        self.graph=dict()
        self.graph_type=graph_type

        #getting list of not required attributes
        att=[attr for attr in dir(data_obj[0]) if ("_" not in attr and attr not in vars(data_obj[0]))]
        #getting list of required attributes 
        required_attributes=list(vars(data_obj[0]).keys())

        for d in data_obj:
            # setting value in hash
            end=getattr(d,required_attributes[1])
            otherData=[]
            for i in required_attributes[2:]:
                otherData.append(getattr(d, i))
            for i in att:
                otherData.append(getattr(d,i))
            connections=({end:otherData})

            # adding entry to hashmap
            if(getattr(d,required_attributes[0]) not in self.graph):
                self.graph.update({getattr(d,required_attributes[0]):[connections]})
            else:
                self.graph[getattr(d,required_attributes[0])].append(connections)
    
    def get_nodes(self):
        return list(self.graph.keys())

    def get_edges(self, node):
        connections = self.graph[node]
        return connections
    
    def value(self, node1, node2):
        print("value ",self.graph[node1])
        for i in self.graph[node1]:
            if(node2 in i.keys()):
                return i[node2][0]
        return 0
            

print(GraphBuilder('_dataset/test.connections.csv',['station1','station2','time'],Directed).graph)
# print()
# print(GraphBuilder('_dataset/london.connections.csv',['station1','station2','time'],Connection).get_nodes())
# print()
# print(GraphBuilder('_dataset/london.connections.csv',['station1','station2','time'],Connection).value(11,83))

# print(GraphBuilder('_dataset/london.stations.csv',['id'],Station).graph)
