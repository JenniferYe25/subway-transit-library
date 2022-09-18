from DataExtractor import DataExtractor
from Connection import Connection
from Station import Station

class GraphBuilder:
    def __init__(self,path,required,graph_type):
        data=DataExtractor()
        data_obj=data.extractRows(path,required,graph_type)
        self.graph=dict()
        print(data_obj)
        #getting list of not required attributes
        att=[attr for attr in dir(data_obj[0]) if ("_" not in attr and attr not in vars(data_obj[0]))]
        #getting list of required attributes 
        required_attributes=list(vars(data_obj[0]).keys())

        for d in data_obj:
            # setting value in hash
            otherData=[]
            for i in required_attributes[1:]:
                otherData.append(getattr(d, i))
            for i in att:
                otherData.append(getattr(d,i))

            # adding entry to hashmap
            if(d.key not in self.graph):
                self.graph.update({getattr(d,required_attributes[0]):[otherData]})
            else:
                self.graph[getattr(d,required_attributes[0])].append(otherData)


# print(GraphBuilder('_dataset/london.connections.csv',['station1','station2','time'],Connection).graph)
print(GraphBuilder('_dataset/london.stations.csv',['id'],Station).graph)
